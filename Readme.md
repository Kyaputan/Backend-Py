# 🐍 Python Backend Showcase: Django | FastAPI | Flask

> A beginner-friendly backend journey through three powerful Python frameworks.

## 📘 Introduction

Welcome to the **Python Backend Showcase**, a practical and beginner-focused repository that explores three of the most widely used web backend frameworks in the Python ecosystem:

- 🌐 **Django** – The "batteries-included" full-stack framework.
- ⚡ **FastAPI** – Fast, modern, and built for asynchronous performance.
- 🔥 **Flask** – Lightweight, flexible, and ideal for microservices.

Whether you're just starting your backend journey or exploring which framework suits your project best, this repo will guide you through the core concepts and implementation of each.

## 🏗️ Project Structure

```bash
python-backend-showcase/
│
├── django_app/          # Django backend project
│   └── ...              # Views, models, admin, etc.
│
├── fastapi_app/         # FastAPI backend project
│   └── ...              # Routes, dependencies, etc.
│
├── flask_app/           # Flask backend project
│   └── ...              # Blueprints, routes, etc.
│
├── requirements.txt     # Shared dependencies for all apps
└── README.md            # You're reading it now!
```

## 🧰 Tech Stack

| Feature | Django | FastAPI | Flask |
|---------|--------|---------|-------|
| Routing | ✅ URL patterns | ✅ Path operations | ✅ Route decorators |
| ORM | ✅ Django ORM | 🔄 SQLAlchemy/Tortoise (Optional) | 🔄 SQLAlchemy (Optional) |
| Admin Panel | ✅ Built-in | ❌ (use 3rd party) | ❌ (build manually) |
| Async Support | ⚠️ Partial (v4+) | ✅ First-class async | ⚠️ Limited (via extensions) |
| API Docs | ❌ Manual or DRF | ✅ Swagger/OpenAPI | ❌ Manual or Flask-RESTX |
| Learning Curve | 🧠 Steep | 🚀 Moderate | 🎈 Easy |

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/python-backend-showcase.git
cd python-backend-showcase
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # on Windows use: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Each Project

#### ▶️ Django

```bash
cd django_app
python manage.py runserver
```

#### ▶️ FastAPI

```bash
cd fastapi_app
uvicorn main:app --reload
```

#### ▶️ Flask

```bash
cd flask_app
python app.py
```

## 🧪 Features Demonstrated

- CRUD APIs
- JSON response formatting
- URL routing & parameter handling
- Basic database integration (SQLite)
- Error handling and custom responses
- API documentation (FastAPI only)
- Simple form handling (Django)
- Modular app structure

## 📚 Recommended Learning Resources

- [Django Official Docs](https://docs.djangoproject.com/)
- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [Flask Docs](https://flask.palletsprojects.com/)

## ❤️ Contributing

This project is open for contributions! Whether it's bug fixes, new features, or better docs — feel free to fork and submit a PR.

## 📄 License

MIT License © 2025 Rachata Singkhet (Caption)

> "Don't just learn frameworks. Understand the concepts behind them." – Caption