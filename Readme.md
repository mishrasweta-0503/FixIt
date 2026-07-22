# 🛠️ FixIt — Issue Tracking & Service Management Platform

A full-stack Django web application designed for seamlessly logging, tracking, and managing maintenance requests and service tickets. Built with modular Django architecture, secure environment management, and responsive UI components.

---

## 🌟 Key Features

* **User Authentication & Authorization:** Secure user registration, role-based access control, and session management.
* **Ticket Management System:** Complete CRUD functionality for creating, updating, triaging, and resolving service tickets.
* **Dynamic Form Rendering:** Styled cleanly using Django Crispy Forms and Bootstrap 5.
* **Production-Ready Security:** Hidden secrets using `python-dotenv`, production static asset handling via WhiteNoise, and deployment configuration via Gunicorn.
* **Responsive UI:** Clean, modern, mobile-friendly interfaces for dashboard interactions.

---

## 🛠️ Tech Stack

* **Backend:** Python 3, Django 5
* **Frontend:** HTML5, CSS3, JavaScript, Bootstrap 5, Django Crispy Forms
* **Server & Deployment:** Gunicorn, WhiteNoise, Render
* **Database & ORM:** SQLite (Development) / PostgreSQL-ready ORM
* **Environment Management:** Python-Dotenv

---

## 🚀 Local Development Setup

Follow these steps to get a local copy running on your machine:

### 1. Prerequisites
Ensure you have **Python 3.10+** and **Git** installed on your system.

### 2. Clone the Repository
    ```bash
    git clone https://github.com/mishrasweta-0503/FixIt.git
    cd FixIt
    ```

### 3. Set Up Virtual Environment
    python -m venv venv
    source venv/bin/activate (macos)
    venv\Scripts\activate (windows)

### 4. Install Dependencies
    pip install -r requirements.txt

### 5. Configure Environment Variables
    touch .env

    Add the following configuration inside your .env file:

    DJANGO_SECRET_KEY=your-local-development-secret-key
    DEBUG=True

### 6. Run Database Migrations
    python manage.py migrate

### 7. Start the Development Server
    python manage.py runserver
    Visit http://127.0.0.1:8000/ in your browser to view the application!

### 8. Deployment Pipeline
    The application is configured for continuous integration and deployment on Render:
    Build Command: pip install -r requirements.txt && python manage.py collectstatic --no-input && python manage.py migrate
    Start Command: gunicorn fixit.wsgi:application
    Static Assets: Served efficiently using WhiteNoise middleware.