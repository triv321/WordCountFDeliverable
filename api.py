#!/usr/bin/env python3
"""
Flask API backend for PCB Pro website.
Provides REST API endpoints for form submissions and data management.
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
from database import Database
import re

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend requests

db = Database()


def validate_email(email):
    """Validate email format."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


@app.route('/')
def index():
    """API root endpoint."""
    return jsonify({
        'message': 'PCB Pro API',
        'version': '1.0.0',
        'endpoints': {
            'POST /api/contact': 'Submit contact form',
            'GET /api/contacts': 'Get all contacts (admin)',
            'GET /api/stats': 'Get database statistics',
            'POST /api/analytics': 'Track analytics event'
        }
    })


@app.route('/api/contact', methods=['POST'])
def submit_contact():
    """Handle contact form submission."""
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['name', 'email', 'company', 'message']
        for field in required_fields:
            if not data.get(field):
                return jsonify({
                    'success': False,
                    'error': f'Missing required field: {field}'
                }), 400
        
        # Validate email format
        if not validate_email(data['email']):
            return jsonify({
                'success': False,
                'error': 'Invalid email format'
            }), 400
        
        # Add to database
        contact_id = db.add_contact(
            name=data['name'],
            email=data['email'],
            company=data['company'],
            message=data['message']
        )
        
        # Track analytics
        db.track_event('contact_submission', {
            'contact_id': contact_id,
            'company': data['company']
        })
        
        return jsonify({
            'success': True,
            'message': 'Contact form submitted successfully',
            'contact_id': contact_id
        }), 201
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/contacts', methods=['GET'])
def get_contacts():
    """Get all contacts (admin endpoint)."""
    try:
        status = request.args.get('status')
        limit = int(request.args.get('limit', 100))
        
        contacts = db.get_contacts(status=status, limit=limit)
        
        return jsonify({
            'success': True,
            'count': len(contacts),
            'contacts': contacts
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/contacts/<int:contact_id>', methods=['PATCH'])
def update_contact(contact_id):
    """Update contact status."""
    try:
        data = request.get_json()
        status = data.get('status')
        
        if not status:
            return jsonify({
                'success': False,
                'error': 'Status is required'
            }), 400
        
        valid_statuses = ['new', 'contacted', 'completed']
        if status not in valid_statuses:
            return jsonify({
                'success': False,
                'error': f'Invalid status. Must be one of: {valid_statuses}'
            }), 400
        
        db.update_contact_status(contact_id, status)
        
        return jsonify({
            'success': True,
            'message': 'Contact status updated'
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/projects', methods=['GET'])
def get_projects():
    """Get all projects."""
    try:
        status = request.args.get('status')
        projects = db.get_projects(status=status)
        
        return jsonify({
            'success': True,
            'count': len(projects),
            'projects': projects
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/projects', methods=['POST'])
def add_project():
    """Add a new project."""
    try:
        data = request.get_json()
        
        name = data.get('name')
        description = data.get('description', '')
        
        if not name:
            return jsonify({
                'success': False,
                'error': 'Project name is required'
            }), 400
        
        project_id = db.add_project(name, description)
        
        return jsonify({
            'success': True,
            'message': 'Project added successfully',
            'project_id': project_id
        }), 201
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/analytics', methods=['POST'])
def track_analytics():
    """Track analytics event."""
    try:
        data = request.get_json()
        
        event_type = data.get('event_type')
        event_data = data.get('event_data')
        
        if not event_type:
            return jsonify({
                'success': False,
                'error': 'event_type is required'
            }), 400
        
        db.track_event(event_type, event_data)
        
        return jsonify({
            'success': True,
            'message': 'Event tracked'
        }), 201
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Get database statistics."""
    try:
        stats = db.get_stats()
        
        return jsonify({
            'success': True,
            'stats': stats
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    return jsonify({
        'status': 'healthy',
        'database': 'connected'
    })


if __name__ == '__main__':
    print("=" * 60)
    print("PCB Pro API Server")
    print("=" * 60)
    print("\nInitializing database...")
    db.init_database()
    print("✓ Database initialized")
    print("\nStarting server...")
    print("API available at: http://localhost:5000")
    print("API documentation: http://localhost:5000/")
    print("\nPress Ctrl+C to stop")
    print("=" * 60 + "\n")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
