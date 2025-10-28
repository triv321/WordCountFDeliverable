#!/usr/bin/env python3
"""
Database module for PCB Pro website.
Uses SQLite for free, serverless data storage.
"""

import sqlite3
import json
from datetime import datetime
from pathlib import Path

DATABASE_PATH = Path(__file__).parent / "pcb_pro.db"


class Database:
    """Database handler for PCB Pro website."""
    
    def __init__(self, db_path=DATABASE_PATH):
        """Initialize database connection."""
        self.db_path = db_path
        self.init_database()
    
    def get_connection(self):
        """Get database connection."""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn
    
    def init_database(self):
        """Initialize database tables."""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        # Create contacts table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                company TEXT NOT NULL,
                message TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                status TEXT DEFAULT 'new'
            )
        """)
        
        # Create projects table (for potential future use)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS projects (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                status TEXT DEFAULT 'active',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Create analytics table (for tracking website metrics)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS analytics (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                event_type TEXT NOT NULL,
                event_data TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        conn.commit()
        conn.close()
    
    def add_contact(self, name, email, company, message):
        """Add a new contact submission."""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO contacts (name, email, company, message)
            VALUES (?, ?, ?, ?)
        """, (name, email, company, message))
        
        contact_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        return contact_id
    
    def get_contacts(self, status=None, limit=100):
        """Get contact submissions."""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        if status:
            cursor.execute("""
                SELECT * FROM contacts 
                WHERE status = ? 
                ORDER BY created_at DESC 
                LIMIT ?
            """, (status, limit))
        else:
            cursor.execute("""
                SELECT * FROM contacts 
                ORDER BY created_at DESC 
                LIMIT ?
            """, (limit,))
        
        contacts = [dict(row) for row in cursor.fetchall()]
        conn.close()
        
        return contacts
    
    def update_contact_status(self, contact_id, status):
        """Update contact status (new, contacted, completed)."""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
            UPDATE contacts 
            SET status = ? 
            WHERE id = ?
        """, (status, contact_id))
        
        conn.commit()
        conn.close()
    
    def add_project(self, name, description):
        """Add a new project."""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO projects (name, description)
            VALUES (?, ?)
        """, (name, description))
        
        project_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        return project_id
    
    def get_projects(self, status=None):
        """Get projects."""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        if status:
            cursor.execute("""
                SELECT * FROM projects 
                WHERE status = ? 
                ORDER BY created_at DESC
            """, (status,))
        else:
            cursor.execute("""
                SELECT * FROM projects 
                ORDER BY created_at DESC
            """)
        
        projects = [dict(row) for row in cursor.fetchall()]
        conn.close()
        
        return projects
    
    def track_event(self, event_type, event_data=None):
        """Track analytics events."""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        event_data_json = json.dumps(event_data) if event_data else None
        
        cursor.execute("""
            INSERT INTO analytics (event_type, event_data)
            VALUES (?, ?)
        """, (event_type, event_data_json))
        
        conn.commit()
        conn.close()
    
    def get_stats(self):
        """Get database statistics."""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        # Count contacts by status
        cursor.execute("""
            SELECT status, COUNT(*) as count 
            FROM contacts 
            GROUP BY status
        """)
        contacts_by_status = {row['status']: row['count'] for row in cursor.fetchall()}
        
        # Count total projects
        cursor.execute("SELECT COUNT(*) as count FROM projects")
        total_projects = cursor.fetchone()['count']
        
        # Count analytics events
        cursor.execute("SELECT COUNT(*) as count FROM analytics")
        total_events = cursor.fetchone()['count']
        
        conn.close()
        
        return {
            'contacts_by_status': contacts_by_status,
            'total_projects': total_projects,
            'total_events': total_events
        }
    
    def export_contacts_csv(self, filename='contacts_export.csv'):
        """Export contacts to CSV file."""
        import csv
        
        contacts = self.get_contacts(limit=10000)
        
        with open(filename, 'w', newline='') as csvfile:
            if contacts:
                fieldnames = contacts[0].keys()
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(contacts)
        
        return filename


def demo():
    """Demo database functionality."""
    db = Database()
    
    print("=" * 60)
    print("PCB Pro Database Demo")
    print("=" * 60)
    
    # Add sample contact
    print("\n1. Adding sample contact...")
    contact_id = db.add_contact(
        name="John Smith",
        email="john.smith@techcorp.com",
        company="TechCorp Industries",
        message="Interested in custom PCB design for IoT devices. Need 1000 units."
    )
    print(f"   ✓ Contact added with ID: {contact_id}")
    
    # Get contacts
    print("\n2. Retrieving contacts...")
    contacts = db.get_contacts(limit=5)
    print(f"   ✓ Found {len(contacts)} contact(s)")
    for contact in contacts:
        print(f"   - {contact['name']} ({contact['company']})")
    
    # Add sample project
    print("\n3. Adding sample project...")
    project_id = db.add_project(
        name="IoT Sensor Board",
        description="4-layer PCB for temperature and humidity sensors"
    )
    print(f"   ✓ Project added with ID: {project_id}")
    
    # Track analytics event
    print("\n4. Tracking analytics event...")
    db.track_event("page_view", {"page": "home", "user_agent": "demo"})
    print("   ✓ Event tracked")
    
    # Get stats
    print("\n5. Database statistics...")
    stats = db.get_stats()
    print(f"   ✓ Contacts by status: {stats['contacts_by_status']}")
    print(f"   ✓ Total projects: {stats['total_projects']}")
    print(f"   ✓ Total events: {stats['total_events']}")
    
    print("\n" + "=" * 60)
    print("Database initialized successfully!")
    print(f"Database location: {DATABASE_PATH}")
    print("=" * 60)


if __name__ == '__main__':
    demo()
