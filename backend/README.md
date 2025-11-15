# Horoscope Backend

FastAPI service for generating and sending daily horoscopes via email.

## Quick Start

```bash
docker-compose up -d backend --build
```

## Local Development

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --port 6100 --reload
```

## Core Components

- `main.py` - FastAPI endpoints
- `database.py` - SQLite database (users, horoscope history)
- `horoscope_generator.py` - Gemini API integration
- `email_sender.py` - SMTP email delivery
- `scheduler.py` - Runs daily at 8 AM (Europe/Budapest)
- `zodiac_calculator.py` - Zodiac sign calculation

## API Endpoints

- `GET /` - Health check
- `POST /api/send-horoscope` - Create user & send horoscope
- `POST /api/send-horoscope-by-email` - Send to existing user
- `GET /api/users` - List users
- `DELETE /api/user/{email}` - Delete user

## Required Environment Variables

Set in `backend/.env`:

```
GEMINI_API_KEY=your-key
SMTP_USER=your-email@gmail.com
SMTP_PASSWORD=your-password
```

## Notes

- Database: SQLite at `/app/data/horoscope.db`
- Port: 6100
- Scheduler sends horoscopes daily at 8:00 AM
