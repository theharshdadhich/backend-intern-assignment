# Multi-Language FAQ System

## 📌 Overview

This project is a Django-based FAQ system that provides an API for retrieving frequently asked questions in multiple languages. It integrates with **Google Translate** for automatic translations, **Redis** for caching, and **Django REST Framework (DRF)** for API development. The project also includes an **admin panel** for easy FAQ management and supports **Docker** for seamless deployment.

---

## 🌍 Supported Features

✅ **Multi-language Support:** Automatically translates FAQs using Google Translate API.
✅ **Redis Caching:** Optimized API performance by caching translations.
✅ **Rich Text Formatting:** FAQs can be stored and displayed with proper text styling.
✅ **Admin Panel:** Easily manage FAQs and translations via Django's built-in admin interface.
✅ **REST API:** Exposes endpoints for retrieving FAQs in different languages.
✅ **Docker Support:** Deploy the project using Docker and Docker Compose.
✅ **GitHub CI/CD:** Automated linting and testing with GitHub Actions.

---

## 🛠 Prerequisites

Ensure you have the following installed:

- Python **3.9+**
- Django **5.1.5**
- Redis (if not using Docker)
- Docker & Docker Compose (for containerized deployment)

---

## 📥 Installation

1. Clone the repository
   ```
   git clone <repository-url>
   cd <project-directory>
   ```
2. Set up a virtual environment and install dependencies
   ``` 
    pip install -r requirements.txt
   
  ```
3. Apply database migrations
  ```
    python manage.py makemigrations
    python manage.py migrate
  ```
4. Create a superuser
    ```
    python manage.py createsuperuser
    ```
5. Run the development server
  ```
    python manage.py runserver
  ```

📡 API Endpoints

🔹 Admin Panel

Access the Django admin panel at:

http://127.0.0.1:8000/admin

🔹 Retrieve FAQs

Get FAQs in a specific language:

GET /api/faqs/?lang=<language_code>

Example Request (Default Language - English):

GET http://127.0.0.1:8000/api/faqs

🏃 Setting Up Redis for Caching

If using Redis separately, pull and run the Redis container:

docker pull redis
docker run --name redis-cache -d -p 6379:6379 redis

This starts both the Django application and Redis container.
