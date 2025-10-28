# PCB Pro - Database Documentation

## Overview

The PCB Pro website uses **SQLite** as a free, serverless database solution for storing contact form submissions, project data, and analytics. SQLite is perfect for this use case because:

- ✅ **100% Free** - No cost, no subscriptions, no limits
- ✅ **Zero Configuration** - No server setup required
- ✅ **Portable** - Single file database
- ✅ **Reliable** - Battle-tested and widely used
- ✅ **Fast** - Excellent performance for small to medium datasets

## Architecture

```
┌─────────────────┐
│   Website       │
│  (HTML/CSS/JS)  │
└────────┬────────┘
         │
         │ HTTP Requests
         ▼
┌─────────────────┐
│   Flask API     │
│  (Python/REST)  │
└────────┬────────┘
         │
         │ SQL Queries
         ▼
┌─────────────────┐
│  SQLite DB      │
│ (pcb_pro.db)    │
└─────────────────┘
```

## Files

- **`database.py`** - Database module with all data operations
- **`api.py`** - Flask REST API server
- **`pcb_pro.db`** - SQLite database file (auto-created)
- **`admin.html`** - Admin dashboard for viewing data

## Database Schema

### Table: `contacts`

Stores contact form submissions from potential customers.

| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER | Primary key (auto-increment) |
| name | TEXT | Contact's full name |
| email | TEXT | Contact's email address |
| company | TEXT | Company name |
| message | TEXT | Project details/inquiry |
| created_at | TIMESTAMP | Submission timestamp |
| status | TEXT | new/contacted/completed |

### Table: `projects`

Stores project records (for future expansion).

| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER | Primary key (auto-increment) |
| name | TEXT | Project name |
| description | TEXT | Project description |
| status | TEXT | active/completed/cancelled |
| created_at | TIMESTAMP | Creation timestamp |

### Table: `analytics`

Tracks website analytics events.

| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER | Primary key (auto-increment) |
| event_type | TEXT | Event type (page_view, contact_submission, etc.) |
| event_data | TEXT | JSON data for the event |
| created_at | TIMESTAMP | Event timestamp |

## Setup & Installation

### 1. Install Dependencies

```bash
# Install Flask and Flask-CORS
pip install -r requirements.txt
```

### 2. Initialize Database

The database is automatically initialized when you first run the API server or database module:

```bash
# Option 1: Run the API server (recommended)
python3 api.py

# Option 2: Run database module directly
python3 database.py
```

This creates the `pcb_pro.db` file with all necessary tables.

### 3. Start the API Server

```bash
python3 api.py
```

The API will be available at `http://localhost:5000`

### 4. Open the Website

```bash
# Option 1: Open directly
open index.html

# Option 2: Use a local server
python3 -m http.server 8000
# Visit http://localhost:8000
```

### 5. Access Admin Dashboard

Open `admin.html` in your browser to view and manage submissions.

## API Endpoints

### Contact Submissions

**POST /api/contact**
Submit a new contact form

```bash
curl -X POST http://localhost:5000/api/contact \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Smith",
    "email": "john@example.com",
    "company": "TechCorp",
    "message": "Need custom PCB design"
  }'
```

Response:
```json
{
  "success": true,
  "message": "Contact form submitted successfully",
  "contact_id": 1
}
```

**GET /api/contacts**
Get all contact submissions

```bash
# Get all contacts
curl http://localhost:5000/api/contacts

# Filter by status
curl http://localhost:5000/api/contacts?status=new

# Limit results
curl http://localhost:5000/api/contacts?limit=10
```

**PATCH /api/contacts/:id**
Update contact status

```bash
curl -X PATCH http://localhost:5000/api/contacts/1 \
  -H "Content-Type: application/json" \
  -d '{"status": "contacted"}'
```

### Projects

**GET /api/projects**
Get all projects

```bash
curl http://localhost:5000/api/projects
```

**POST /api/projects**
Add a new project

```bash
curl -X POST http://localhost:5000/api/projects \
  -H "Content-Type: application/json" \
  -d '{
    "name": "IoT Sensor Board",
    "description": "4-layer PCB design"
  }'
```

### Analytics

**POST /api/analytics**
Track an analytics event

```bash
curl -X POST http://localhost:5000/api/analytics \
  -H "Content-Type: application/json" \
  -d '{
    "event_type": "page_view",
    "event_data": {"page": "home"}
  }'
```

**GET /api/stats**
Get database statistics

```bash
curl http://localhost:5000/api/stats
```

Response:
```json
{
  "success": true,
  "stats": {
    "contacts_by_status": {
      "new": 5,
      "contacted": 3,
      "completed": 2
    },
    "total_projects": 10,
    "total_events": 150
  }
}
```

### Health Check

**GET /health**
Check API health

```bash
curl http://localhost:5000/health
```

## Usage Examples

### Python Usage

```python
from database import Database

# Initialize database
db = Database()

# Add a contact
contact_id = db.add_contact(
    name="Jane Doe",
    email="jane@company.com",
    company="Company Inc",
    message="Need 500 PCBs for production"
)

# Get all new contacts
new_contacts = db.get_contacts(status='new')
for contact in new_contacts:
    print(f"{contact['name']} from {contact['company']}")

# Update contact status
db.update_contact_status(contact_id, 'contacted')

# Get statistics
stats = db.get_stats()
print(f"Total contacts: {sum(stats['contacts_by_status'].values())}")

# Track analytics
db.track_event('quote_requested', {'amount': 1000})

# Export contacts to CSV
db.export_contacts_csv('contacts.csv')
```

### JavaScript Usage

```javascript
// Submit contact form
async function submitContact(data) {
    const response = await fetch('http://localhost:5000/api/contact', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(data)
    });
    return await response.json();
}

// Track page view
async function trackPageView() {
    await fetch('http://localhost:5000/api/analytics', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
            event_type: 'page_view',
            event_data: {page: window.location.pathname}
        })
    });
}
```

## Database Management

### Backup Database

```bash
# Simple copy
cp pcb_pro.db pcb_pro_backup.db

# Or use SQLite dump
sqlite3 pcb_pro.db .dump > backup.sql
```

### Restore Database

```bash
# From backup file
cp pcb_pro_backup.db pcb_pro.db

# From SQL dump
sqlite3 pcb_pro.db < backup.sql
```

### View Database

```bash
# Open SQLite CLI
sqlite3 pcb_pro.db

# Run queries
sqlite> SELECT * FROM contacts;
sqlite> SELECT COUNT(*) FROM contacts WHERE status='new';
sqlite> .schema contacts
sqlite> .exit
```

### Export Data

```python
# Export contacts to CSV
from database import Database
db = Database()
db.export_contacts_csv('contacts_export.csv')
```

## Production Deployment

### Option 1: Keep SQLite (Recommended for Small Scale)

SQLite works great for:
- Small to medium traffic websites
- Up to ~100,000 records
- Read-heavy workloads

No changes needed - just deploy the files!

### Option 2: Upgrade to PostgreSQL/MySQL

For larger scale, you can easily migrate to PostgreSQL or MySQL:

1. Export data using Python's SQLAlchemy
2. Update connection string in `database.py`
3. Re-run initialization

### Option 3: Cloud Database

Use managed database services:
- **Railway** - Free PostgreSQL tier
- **PlanetScale** - Free MySQL tier
- **Supabase** - Free PostgreSQL with API
- **MongoDB Atlas** - Free NoSQL tier

## Security Notes

### For Production:

1. **Add Authentication**
   - Protect admin endpoints with API keys
   - Use JWT tokens for authentication

2. **Input Validation**
   - Already implemented basic validation
   - Add rate limiting for API endpoints

3. **CORS Configuration**
   - Update `api.py` to restrict CORS to your domain
   ```python
   CORS(app, origins=['https://yourdomain.com'])
   ```

4. **Environment Variables**
   - Move sensitive config to `.env` file
   ```python
   API_KEY = os.getenv('API_KEY')
   ```

5. **HTTPS**
   - Use SSL/TLS in production
   - Deploy behind reverse proxy (nginx)

## Troubleshooting

### Database locked error
```bash
# Close all connections and try again
rm pcb_pro.db-journal
```

### API not accessible
```bash
# Check if server is running
ps aux | grep api.py

# Check if port 5000 is available
lsof -i :5000
```

### CORS errors
- Make sure Flask-CORS is installed
- Check browser console for specific errors
- Verify API_URL in `script.js` matches server

## Performance Tips

1. **Index frequently queried columns**
```sql
CREATE INDEX idx_contacts_status ON contacts(status);
CREATE INDEX idx_contacts_created ON contacts(created_at);
```

2. **Use connection pooling** (for high traffic)

3. **Cache frequent queries** (Redis/Memcached)

4. **Archive old data** periodically

## Cost Analysis

**Current Setup (SQLite):**
- Database: $0/month ✅
- Hosting: $0/month (static hosting) ✅
- API Server: $5-10/month (VPS like DigitalOcean)
- **Total: ~$5-10/month**

**Alternative (Cloud Database):**
- Supabase/Railway Free Tier: $0/month
- Heroku/Railway API: $0-5/month
- **Total: $0-5/month**

## Support

For issues or questions:
- Check the troubleshooting section
- Review API endpoint documentation
- Test with `curl` commands
- Check Flask server logs

## License

Part of the PCB Pro platform. See main README for license information.
