# BrandConnect SaaS

## Overview
BrandConnect is a production-ready FastAPI-based SaaS application for user management and authentication, deployed on Heroku with PostgreSQL, GitHub for version control, and automated daily backups.

## Features
- User registration and JWT-based authentication via `/users/create` and `/auth/login`.
- Database management with SQLAlchemy and Alembic migrations.
- Daily automated backups at 2:00 AM UTC via Heroku Scheduler.
- Logging for monitoring endpoint access and performance optimization.

## Installation
1. Clone the repository: `git clone https://github.com/knsholdings/brandconnect-saas`
2. Navigate to the directory: `cd brandconnect-saas`
3. Set up a virtual environment: `python -m venv venv`
4. Activate it: `.\venv\Scripts\Activate.ps1` (Windows)
5. Install dependencies: `pip install -r requirements.txt`
6. Configure PostgreSQL locally and set up `alembic.ini` with your database URL.

## Deployment
- Deploy to Heroku using `git push heroku main` after setting up `Procfile`, `requirements.txt`, and environment variables (e.g., `SECRET_KEY`, `DATABASE_URL`).
- Monitor with `heroku logs --tail -a brandconnect-saas`.
- Ensure Heroku Scheduler is configured for daily backups.

## Backups
- Backups run daily at 2:00 AM UTC, storing SQL dumps. Verify via Heroku Scheduler dashboard and logs (first successful run on February 27, 2025).

## Testing
- Use Postman to test endpoints: `POST https://brandconnect-saas-9bde66e6c0c4.herokuapp.com/users/create` and `POST https://brandconnect-saas-9bde66e6c0c4.herokuapp.com/auth/login`.
- Ensure Firefox shows the app at `https://brandconnect-saas-9bde66e6c0c4.herokuapp.com`.

## Production Notes
- Optimized for Heroku’s paid dyno (1 Gunicorn worker, database pooling with Heroku PostgreSQL:essential-0).
- Monitor logs and backups regularly for production stability.
- Security: Rotate `SECRET_KEY` periodically and avoid committing sensitive data to GitHub.