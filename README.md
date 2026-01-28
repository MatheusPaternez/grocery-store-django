# Paternez Store

Professional Django e-commerce sample application for demonstration and small deployments.

---

## Table of Contents

- Project Overview
- Features
- Tech Stack
- Quick Start
  - Requirements
  - Setup (Windows)
  - Run development server
- Data & Database
- Project Structure
- Testing
- Deployment Notes
- License & Contact

---

## Project Overview

Paternez Store is a Django-based web application implementing a small online store. It includes product listing, order management, user accounts, and a simple admin interface. The project is intended as a practical example for learning, prototyping, or small projects.

## Features

- Product catalog and detail pages
- Shopping cart and order flow
- Accounts and authentication
- Admin interface for managing products, orders, and users
- Basic templates and static assets

## Tech Stack

- Python: 3.13 (virtual environment used in this repository)
- Django: 6.0.x (installed in the environment)
- Database: SQLite (default file `db.sqlite3`)

Dependencies are managed with `pip` and a `requirements.txt` file.

## Quick Start

These instructions assume you are working on Windows and using a virtual environment. Adjust commands for macOS/Linux as needed.

### Requirements

- Python 3.11+ (this repository's virtualenv shows Python 3.13.9)
- pip

### Setup (Windows)

1. Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1    # PowerShell
# or
.\.venv\Scripts\activate.bat    # cmd.exe
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Apply migrations and create a superuser:

```powershell
python manage.py migrate
python manage.py createsuperuser
```

4. (Optional) Load sample data if `data.json` exists:

```powershell
python manage.py loaddata data.json
```

### Run development server

```powershell
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser. Access the admin at http://127.0.0.1:8000/admin/.

## Data & Database

The project ships with `db.sqlite3` as the default database file for simple local development. To move to a production-ready database (Postgres, MySQL), update `paternezStore/settings.py` and provide appropriate environment variables.

If you have `data.json` in the repository, it can be loaded with `python manage.py loaddata data.json` to pre-populate products or other fixtures.

## Project Structure (top-level)

- `manage.py` - Django CLI entrypoint
- `db.sqlite3` - default local SQLite database
- `paternezStore/` - Django project settings and WSGI/ASGI
- `accounts/`, `core/`, `orders/`, `products/` - application modules
- `static/` - static assets
- `templates/` - shared templates (e.g., `master.html`)

Explore individual app folders for models, views, and templates.

## Testing

Run Django tests with:

```powershell
python manage.py test
```

Add unit tests in each app's `tests.py` or in a `tests/` package.

## Deployment Notes

This repository is configured for local development. For production deployment consider:

- Use a production-grade WSGI/ASGI server (Gunicorn, Daphne, etc.) behind a reverse proxy
- Use PostgreSQL or another robust DB instead of SQLite
- Configure `DEBUG = False` and set a secure `SECRET_KEY` via environment variables
- Set `ALLOWED_HOSTS` to your domain names
- Serve static files via `collectstatic` to a CDN or web server

## Environment Variables

At runtime, provide the following environment variables for a secure production setup:

- `SECRET_KEY` - Django secret key
- `DEBUG` - `False` in production
- `DATABASE_URL` - optional, if using a non-default DB
- `ALLOWED_HOSTS` - comma-separated hostnames

## License

Specify the project license here (e.g., MIT, Apache 2.0). If you have no license file, add one to make reuse terms explicit.

## Contact

For questions or help, open an issue in the repository or contact the maintainer.

---

If you'd like, I can also:

- add environment variable support via `python-decouple` or `django-environ`
- create a `Procfile` and simple `docker-compose.yml` for deployment
- generate a small CONTRIBUTING.md and CODE_OF_CONDUCT.md

---

Last updated: January 28, 2026
