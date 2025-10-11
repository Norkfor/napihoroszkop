from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr, Field
from sqlalchemy.orm import Session
from datetime import datetime
from horoscope_generator import generate_horoscope
from email_sender import send_email
from zodiac_calculator import get_zodiac_sign
from database import init_db, get_db, User
from scheduler import start_scheduler
import time

app = FastAPI(title="Zodiac_API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

init_db()

start_scheduler()


class HoroscopeRequest(BaseModel):
    name: str
    email: EmailStr
    birth_month: int = Field(..., ge=1, le=12, description="Birth month (1-12)")
    birth_day: int = Field(..., ge=1, le=31, description="Birth day (1-31)")

@app.get("/")
def root():
    return {"message": "API is working! Scheduler active."}

@app.post("/api/send-horoscope")
def send_horoscope_endpoint(request: HoroscopeRequest, db: Session = Depends(get_db)):
    try:
        zodiac_sign = get_zodiac_sign(request.birth_month, request.birth_day)
        
        existing_user = db.query(User).filter(User.email == request.email).first()
        
        if existing_user:
            existing_user.name = request.name
            existing_user.birth_month = request.birth_month
            existing_user.birth_day = request.birth_day
            existing_user.zodiac_sign = zodiac_sign
            existing_user.last_horoscope_sent = datetime.now()
            db.commit()
            user_id = existing_user.id
        else:
            new_user = User(
                name=request.name,
                email=request.email,
                birth_month=request.birth_month,
                birth_day=request.birth_day,
                zodiac_sign=zodiac_sign,
                last_horoscope_sent=datetime.now()
            )
            db.add(new_user)
            db.commit()
            db.refresh(new_user)
            user_id = new_user.id
        
        horoscope_html = generate_horoscope(zodiac_sign, request.name)
        send_email(request.email, zodiac_sign, horoscope_html)
        
        return {
            "success": True,
            "zodiac_sign": zodiac_sign,
            "message": f"Horoscope sent to {request.name} ({zodiac_sign}) at {request.email}!",
            "user_id": user_id
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail="Invalid birth date")
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

@app.post("/api/send-all-horoscopes")
def send_all_horoscopes(db: Session = Depends(get_db)):
    try:
        users = db.query(User).all()
        
        if not users:
            return {
                "success": False,
                "message": "No users in database"
            }
        
        results = {
            "total_users": len(users),
            "sent": 0,
            "failed": 0,
            "details": []
        }
        
        for user in users:
            try:
                horoscope_html = generate_horoscope(user.zodiac_sign, user.name)
                send_email(user.email, user.zodiac_sign, horoscope_html)
                
                user.last_horoscope_sent = datetime.now()
                db.commit()
                
                results["sent"] += 1
                results["details"].append({
                    "email": user.email,
                    "name": user.name,
                    "status": "success"
                })
                
                time.sleep(1)
                
            except Exception as e:
                results["failed"] += 1
                results["details"].append({
                    "email": user.email,
                    "name": user.name,
                    "status": "failed",
                    "error": str(e)
                })
        
        return {
            "success": True,
            "message": f"Sent {results['sent']} horoscopes, {results['failed']} failed",
            "results": results
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

@app.get("/api/users")
def get_all_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return {
        "total": len(users), 
        "users": [
            {
                "id": user.id,
                "name": user.name,
                "email": user.email,
                "birth_month": user.birth_month,
                "birth_day": user.birth_day,
                "zodiac_sign": user.zodiac_sign,
                "created_at": user.created_at,
                "last_horoscope_sent": user.last_horoscope_sent
            } for user in users
        ]
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=6100)
