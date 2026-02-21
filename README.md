# HR Attendance Management System – Backend

## 📌 Project Overview

This is the backend API for the HR Attendance Management System.

It provides RESTful APIs to:
- Manage Employees (Create, List, Delete)
- Manage Attendance Records
- Filter attendance by employee and date

The backend is built using Django and Django REST Framework and is deployed on Railway with PostgreSQL.

---

## 🛠 Tech Stack Used

- Python 3.8.10
- Django 4.2
- Django REST Framework
- PostgreSQL
- Gunicorn
- django-cors-headers
- Railway (deployment)

---

## 🚀 Steps to Run the Project Locally

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Tapesh-1308/HRMS-Backend.git backend

cd backend
````

### 2️⃣ Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Create `.env` file

Create a `.env` file in the root directory:

```
DEBUG=False
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=5432
SECRET_KEY=
ALLOWED_HOSTS=localhost
```

### 5️⃣ Run migrations

```bash
python manage.py migrate
```

### 6️⃣ Run development server

```bash
python manage.py runserver
```

Server will run at:

```
http://127.0.0.1:8000/
```

---

## ⚠ Assumptions & Limitations

* No authentication system implemented.
* Pagination not enabled by default.
* Designed for demonstration purposes (not production-grade security hardening).

---

## 🌍 Deployment

* Hosted on Railway
* Uses PostgreSQL in production
* Environment variables are configured via Railway dashboard
