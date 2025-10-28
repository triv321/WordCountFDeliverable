# PCB Pro - Quick Start Guide

## 🚀 Get Started in 3 Steps

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install flask flask-cors
```

### Step 2: Start the API Server

```bash
# Option 1: Using the startup script
./start_api.sh

# Option 2: Direct Python command
python3 api.py
```

The API will start on `http://localhost:5000`

### Step 3: Open the Website

```bash
# Option 1: Open directly in browser
open index.html

# Option 2: Use Python's HTTP server
python3 -m http.server 8000
# Then visit http://localhost:8000
```

## 📋 What You Get

### 1. Main Website (`index.html`)
- Professional PCB sales landing page
- Responsive design (mobile, tablet, desktop)
- Smooth animations
- Contact form with database integration

### 2. Admin Dashboard (`admin.html`)
- View all contact submissions
- Filter by status
- Update contact status
- View statistics

### 3. Database (`pcb_pro.db`)
- Automatically created SQLite database
- Stores contacts, projects, and analytics
- No configuration needed
- 100% free

### 4. REST API (`api.py`)
- RESTful endpoints for all operations
- CORS enabled for frontend requests
- Automatic data validation
- JSON responses

## 🧪 Test the System

### Test Database
```bash
python3 database.py
```

You should see:
```
============================================================
PCB Pro Database Demo
============================================================
1. Adding sample contact...
✓ Contact added with ID: 1
...
```

### Test API
```bash
# Start API server
python3 api.py

# In another terminal, test endpoints:
curl http://localhost:5000/health
curl http://localhost:5000/api/stats
```

### Test Contact Form
1. Open `index.html` in browser
2. Fill out the contact form
3. Submit
4. Open `admin.html` to see the submission

## 📁 Project Structure

```
.
├── index.html              # Main website
├── styles.css              # Website styling
├── script.js               # Frontend JavaScript
├── admin.html              # Admin dashboard
├── database.py             # Database module
├── api.py                  # Flask API server
├── start_api.sh            # API startup script
├── pcb_pro.db              # SQLite database (auto-created)
├── requirements.txt        # Python dependencies
├── PCB_WEBSITE_README.md   # Website documentation
├── DATABASE_README.md      # Database documentation
└── QUICK_START.md          # This file
```

## 🌐 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | API info |
| GET | `/health` | Health check |
| POST | `/api/contact` | Submit contact form |
| GET | `/api/contacts` | Get all contacts |
| PATCH | `/api/contacts/:id` | Update contact status |
| GET | `/api/projects` | Get all projects |
| POST | `/api/projects` | Add new project |
| POST | `/api/analytics` | Track analytics event |
| GET | `/api/stats` | Get statistics |

## 💡 Common Tasks

### Add a Contact (via API)
```bash
curl -X POST http://localhost:5000/api/contact \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Doe",
    "email": "john@company.com",
    "company": "Tech Corp",
    "message": "Need 1000 PCBs"
  }'
```

### View All Contacts
```bash
curl http://localhost:5000/api/contacts
```

### Get Statistics
```bash
curl http://localhost:5000/api/stats
```

### Export Contacts to CSV
```python
from database import Database
db = Database()
db.export_contacts_csv('contacts.csv')
```

## 🐛 Troubleshooting

### "Module not found" error
```bash
# Make sure Flask is installed
pip install flask flask-cors
```

### "Address already in use" error
```bash
# Kill existing process on port 5000
lsof -ti:5000 | xargs kill -9
```

### Database locked error
```bash
# Remove journal file
rm pcb_pro.db-journal
```

### CORS errors in browser
- Make sure API server is running
- Check that API_URL in script.js is correct
- Verify Flask-CORS is installed

## 🎨 Customization

### Change Colors
Edit CSS variables in `styles.css`:
```css
:root {
    --primary-color: #0066FF;  /* Your color here */
    --secondary-color: #00FF88;
}
```

### Change API Port
Edit `api.py`:
```python
app.run(debug=True, host='0.0.0.0', port=5000)  # Change port
```

Then update `script.js`:
```javascript
const API_URL = 'http://localhost:5000';  // Update port
```

### Add More Database Tables
Edit `database.py` and add new tables in `init_database()` method.

## 📊 Viewing the Database

### Using SQLite CLI
```bash
sqlite3 pcb_pro.db

sqlite> .tables
sqlite> SELECT * FROM contacts;
sqlite> .schema contacts
sqlite> .exit
```

### Using Python
```python
from database import Database
db = Database()

# Get all contacts
contacts = db.get_contacts()
for contact in contacts:
    print(contact)

# Get statistics
stats = db.get_stats()
print(stats)
```

## 🚀 Next Steps

1. ✅ Test the website locally
2. ✅ Submit test contact forms
3. ✅ View data in admin dashboard
4. 🔄 Customize colors and content
5. 🔄 Add your own domain
6. 🔄 Deploy to hosting service
7. 🔄 Set up backups for database

## 📚 More Information

- **Website Documentation**: `PCB_WEBSITE_README.md`
- **Database Documentation**: `DATABASE_README.md`
- **Implementation Details**: `IMPLEMENTATION_SUMMARY.md`

## 💰 Cost

Everything is **100% free**:
- ✅ SQLite database: Free
- ✅ Frontend (static files): Free to host
- ✅ Python/Flask: Free and open source
- ✅ No monthly subscriptions
- ✅ No usage limits

**Optional hosting costs:**
- Static hosting (Netlify/Vercel): $0/month
- API hosting (DigitalOcean/Railway): $5-10/month

## 🆘 Need Help?

1. Check the troubleshooting section
2. Review the documentation files
3. Test with curl commands
4. Check API server logs

## ✨ Features

- ✅ Fully responsive design
- ✅ Smooth animations
- ✅ Contact form with validation
- ✅ SQLite database
- ✅ REST API
- ✅ Admin dashboard
- ✅ Analytics tracking
- ✅ Zero dependencies (frontend)
- ✅ Professional design
- ✅ B2B focused content

Enjoy your PCB sales website! 🎉
