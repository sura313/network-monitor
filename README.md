# 🌐 Network Monitor

> A real-time network device monitoring dashboard built with Django, Celery, and PostgreSQL. Monitor servers, routers, and any networked device — get instant status updates and email alerts when devices go offline.

![Python](https://img.shields.io/badge/Python-3.13-blue?style=flat-square&logo=python)
![Django](https://img.shields.io/badge/Django-6.0-green?style=flat-square&logo=django)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-blue?style=flat-square&logo=postgresql)
![Celery](https://img.shields.io/badge/Celery-5.3-brightgreen?style=flat-square)
![Redis](https://img.shields.io/badge/Redis-7.0-red?style=flat-square&logo=redis)

---

## 📸 Screenshots

### Dashboard — Live Device Status
![Dashboard](https://raw.githubusercontent.com/sura313/network-monitor/main/screenshots/dashboard.png)

---

## ✨ Features

- **Real-time ping monitoring** — checks any device by IP address using ICMP ping
- **Live status dashboard** — color-coded online/offline/unknown indicators with response times
- **Auto-refresh** — dashboard refreshes every 30 seconds automatically
- **Email alerts** — sends instant email notification when a device goes offline
- **Ping history logs** — stores every ping result per device for audit trails
- **One-click ping** — manually trigger a check on any device instantly
- **Check All** — ping every monitored device with a single click
- **Background tasks** — Celery + Redis powers scheduled auto-monitoring
- **Responsive dark UI** — clean professional interface built with pure CSS

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python 3.13, Django 6.0 |
| Database | PostgreSQL 16 |
| Task Queue | Celery 5.3 + Redis |
| Scheduling | django-celery-beat |
| Email | Django SMTP (Gmail) |
| Frontend | HTML5, CSS3 (no framework) |
| Deployment | Railway / Gunicorn / Whitenoise |

---

## 🏗️ Project Structure

```
network_monitor/
├── core/
│   ├── settings.py       # Django config, Celery config, email config
│   ├── urls.py           # Root URL routing
│   └── celery.py         # Celery app initialization
├── monitor/
│   ├── models.py         # Device + PingLog models
│   ├── views.py          # Dashboard, ping, add/delete device views
│   ├── utils.py          # Ping logic + email alert sender
│   ├── forms.py          # DeviceForm
│   ├── urls.py           # App URL routing
│   ├── admin.py          # Admin panel registration
│   └── templates/
│       ├── dashboard.html      # Main monitoring dashboard
│       ├── add_device.html     # Add new device form
│       └── device_detail.html  # Device ping history logs
├── manage.py
├── requirements.txt
└── Procfile              # Railway/Heroku deployment
```

---

## ⚙️ How It Works

```
User visits dashboard
        ↓
Django view queries all Device objects from PostgreSQL
        ↓
Dashboard renders with live status, response times, last checked time
        ↓
User clicks "Ping" → Django calls ping_device(ip_address)
        ↓
subprocess.run(['ping', '-n', '1', ip]) → returns online/offline + ms
        ↓
Device status updated in DB → PingLog entry created
        ↓
If status changed to offline → send_alert_email() fires
        ↓
Dashboard auto-refreshes every 30s showing updated status
```

---

## 🚀 Local Setup

### Prerequisites
- Python 3.10+
- PostgreSQL
- Redis (for Celery)

### Installation

```bash
# Clone the repo
git clone https://github.com/sura313/network-monitor.git
cd network-monitor

# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your database and email credentials

# Run migrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Start the server
python manage.py runserver
```

### Environment Variables

Create a `.env` file in the root:

```env
SECRET_KEY=your-secret-key
DEBUG=True
DB_NAME=network_monitor
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=127.0.0.1
DB_PORT=5432
EMAIL_HOST_USER=your_gmail@gmail.com
EMAIL_HOST_PASSWORD=your_gmail_app_password
```

### Running Celery (for background tasks)

```bash
# In a separate terminal
celery -A core worker --loglevel=info

# For scheduled tasks
celery -A core beat --loglevel=info
```

---

## 📡 Devices You Can Monitor

- Web servers (any public IP or domain)
- Local network devices (routers, switches)
- Google DNS: `8.8.8.8`
- Your own server: `192.168.x.x`
- Any device reachable by IP

---

## 🔗 Related Projects

- [Bank Transaction Dashboard](https://github.com/sura313/bank-transaction-dashboard) — Django + PostgreSQL financial tracker
- [Loan Tracker REST API](https://github.com/sura313/loan-tracker-api) — Django REST Framework + JWT authentication

---

## 👨‍💻 Author

**Surafel Dagne Sewenet**
- IT Officer @ Bank of Abyssinia
- B.Sc. Electrical Engineering — Addis Ababa University
- GitHub: [@sura313](https://github.com/sura313)
- Email: sura513533@gmail.com
