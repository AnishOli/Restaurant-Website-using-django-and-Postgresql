# Restaurant Ordering System
## Full Stack Web Application (Django + PostgreSQL)
A **full-stack restaurant ordering platform** built using **Django** and **PostgreSQL**.
The system allows users to browse menu items, authenticate securely, and manage restaurant data through an admin dashboard.
This project demonstrates backend development, authentication workflows, database design, and image handling in a production-style web application.

## ✨ Features
### User Features
- User registration and authentication

- Login / logout functionality

- Browse restaurant menu

- View food item details

- Image-based menu items

- Responsive UI

## Admin Features
- Admin dashboard

- Add / edit / delete food items

- Manage users

- Manage menu database

- Upload images for food items

## 🧠 System Architecture
```
User Request
     ↓
Django URL Routing
     ↓
Views (Business Logic)
     ↓
Models (Database ORM)
     ↓
PostgreSQL Database
     ↓
Templates (HTML Rendering)
     ↓
Response Returned to User
```
## 🧰 Tech Stack
### Backend
- Python
- Django
### Database
- Postgresql
### Authentication
- Django Allauth
- OAuth authentication
## Libraries
- Django
- Django Allauth
- Social Auth Django
- Psycopg2
- Pillow
- Requests
- Python Decouple
- QRCode
### Tools
- Git
- GitHub
- VS Code
## 📦 Requirements
Install dependencies using:
``` 
pip install -r requirements.txt
 ```
Dependencies include:
```
 Django
psycopg2
django-allauth
pillow
qrcode
python-decouple
requests
social-auth-app-django
````
## ⚙️ Installation Guide
### 1️⃣ Clone repository
```
 git clone https://github.com/AnishOli/Restaurant-Website-using-django-and-Postgresql.git
cd Restaurant-Website-using-django-and-Postgresql
 ```
### 2️⃣ Create virtual environment
```
python -m venv myenv
```
Activate environment for windowa:
```
./myenv/Scripts/activate
```
Mac/Linux:
```
source venv/bin/activate
```
### 3️⃣ Install dependencies
```
pip install -r requirements.txt
```
### 4️⃣ Configure environment variables
Create .env
```
SECRET_KEY = you secret_key
DEBUG = True

#social key
SOCIAL_AUTH_URL_NAMESPACE = social
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = google _auth key
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = google_oauth secret
SOCIAL_AUTH_GITHUB_KEY = github key
SOCIAL_AUTH_GITHUB_SECRET = github secret

SOCIAL_AUTH_FACEBOOK_KEY=facebook key
SOCIAL_AUTH_FACEBOOK_SECRET=facebook secret
#end here

# emai setup in django
EMAIL_BACKEND = django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST = smtp.gmail.com
EMAIL_USE_TLS = True
EMAIL_PORT = your email port
EMAIL_HOST_USER = Your host email
EMAIL_HOST_PASSWORD = email host password
# Database

DATABASE_NAME=you restaurant_db
DATABASE_PASSWORD= password
```
### 5️⃣ Run migrations
```
python manage.py makemigrations
python manage.py migrate
```
### 6️⃣ Create admin user
```
python manage.py createsuperuser
```
### 7️⃣ Run development server
```
python manage.py runserver
```
**Open in browser**
```
http://127.0.0.1:8000
```
**Admin panel**
```
http://127.0.0.1:8000/admin
```
## 📂 Project Structure
```
restaurant-website/
│
├── restaurant_project/
│
├── apps/
│   ├── accounts/
│   ├── menu/
│   ├── orders/
│
├── templates/
├── static/
├── media/
│
├── manage.py
├── requirements.txt
└── README.md
```
## 🔒 Security Practices
- Environment variables using ```.env```
- Secure authentication system
- Password hashing with Django auth
- Protected admin panel

## 🚧 Future Improvements
- Payment integration (eSewa / Khalti)
- REST API with Django REST Framework
- Order tracking system
- Table reservation
- Mobile app integration

## Live Demo
[live Link](https://anishmomorestaurant.pythonanywhere.com/)

## ⭐ Support
If you found this project helpful, consider giving it a star **⭐ on GitHub**.
















![Django](https://img.shields.io/badge/Django-6.0-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)
![Python](https://img.shields.io/badge/Python-Backend-yellow)
![License](https://img.shields.io/badge/License-MIT-red)
