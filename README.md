🌍 Supported Features

✅ Multi-language Support: Automatically translates FAQs using Google Translate API.

✅ Redis Caching: Optimized API performance by caching translations.

✅ Rich Text Formatting: FAQs can be stored and displayed with proper text styling.

✅ Admin Panel: Easily manage FAQs and translations via Django's built-in admin interface.

✅ REST API: Exposes endpoints for retrieving FAQs in different languages.

✅ Docker Support: Deploy the project using Docker and Docker Compose.

✅ GitHub CI/CD: Automated linting and testing with GitHub Actions.

✅ AWS Deployment: Hosted on Amazon Web Services (AWS).

🛠 Prerequisites

Ensure you have the following installed:

Python 3.9+

Django 5.1.5

Redis (if not using Docker)

Docker & Docker Compose (for containerized deployment)

📥 Installation

🔹 Running with Docker

To run the project using Docker:

docker-compose up --build

🔹 Manual Setup

Clone the repository

git clone <repository-url>
cd <project-directory>

Set up a virtual environment and install dependencies

python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
pip install -r requirements.txt

Apply database migrations

python manage.py makemigrations
python manage.py migrate

Create a superuser

python manage.py createsuperuser

Run the development server

python manage.py runserver

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

🤝 Contribution Guidelines

We welcome contributions! Follow these steps to contribute:

Fork the repository and create a new branch.

Ensure your code follows PEP8 standards.

Run lint checks before submitting a pull request:

flake8 .

Run tests to confirm functionality:

python manage.py test

Submit a pull request with a detailed description of your changes.

📌 Assumptions & Design Choices

The admin panel displays only English questions for consistency.

Pre-translations are currently supported for Hindi and Bengali.

Future versions may include user-submitted translations for better accuracy.

📜 License

This project is licensed under the MIT License.

