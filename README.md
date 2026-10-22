# ♻️ Swachhta Sahayak – Smart Waste Management (SIH)

A waste-management web app built for **Smart India Hackathon (SIH)** as part of a "Clean City Mission". It connects three kinds of users on one platform:

| Role | Goal |
|------|------|
| 🧑 **Citizen** | Report waste and track collection vehicles |
| 🚛 **Worker** | Manage routes and pickups |
| 🛡️ **Admin** | Monitor complaints and assign tasks |

> 🚧 **Status:** early prototype. The landing page and the three role dashboards are in place; reporting, tracking and task assignment are still to be built.

## 🧱 Tech stack

- **Python / Flask** with Blueprints (one per role)
- **PostgreSQL** via `psycopg2`
- **Tailwind CSS** + Poppins font on the landing page
- PWA icons (`static/icon/192icon.png`, `512icon.png`)

## 📁 Structure

```
├── app.py                 # Flask app, DB connection, registers blueprints
├── templates/index.html   # Landing page – choose Citizen / Worker / Admin
├── citizen/               # /citizen  → citizen_dashboard.html
├── worker/                # /worker   → worker_dashboard.html
├── admin/                 # /admin    → admin_dashboard.html
├── static/                # css, js, icons
└── requirements.txt
```

## 🚀 Run locally

1. Install and start **PostgreSQL**.
2. Update the connection details at the top of `app.py` (`host`, `dbname`, `user`, `password`, `port`).
3. Install dependencies and run:

```bash
git clone https://github.com/Adarshmilan/SIHwastemanagement.git
cd SIHwastemanagement
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install flask psycopg2-binary
python app.py                     # http://127.0.0.1:5000
```

## 🗺️ Routes

| Route | Page |
|-------|------|
| `/` | Landing page with role selection |
| `/citizen` | Citizen dashboard |
| `/worker` | Worker dashboard |
| `/admin` | Admin dashboard |

## 🔮 Planned

- Waste reporting with photo and location
- Live tracking of collection vehicles
- Complaint management and task assignment for admins
- Route and pickup management for workers
