# NapiHoroszkóp

Full-stack app that generates and emails daily horoscopes. Backend (FastAPI) + Frontend (React/Vite).

## Quick Start

```bash
docker-compose up -d --build
```

Access:
- Frontend: `http://localhost:8080`
- Backend: `http://localhost:6100`

## Local Development

**Backend:**
```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --port 6100 --reload
```

**Frontend:**
```bash
cd frontend
npm install
npm run dev
```

## What It Does

- Users sign up with their birth date
- System calculates zodiac sign
- AI generates personalized daily horoscope (Gemini API)
- Emails sent daily at 8 AM (Europe/Budapest)
- REST API for user & horoscope management

## Setup

Create `backend/.env`:
```
GEMINI_API_KEY=your-gemini-key
SMTP_USER=your-email@gmail.com
SMTP_PASSWORD=your-app-password
```

## Technology

- **Backend**: FastAPI, SQLAlchemy, SQLite, Python
- **Frontend**: React, Vite
- **Scheduler**: APScheduler (daily at 8 AM)
- **Containerization**: Docker & Docker Compose

## Structure

```
backend/    - FastAPI service
frontend/   - React UI
```

See individual READMEs in each folder for details.
