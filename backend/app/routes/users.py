from fastapi import APIRouter, Depends
from backend.app.services.auth import hash_password
from backend.app.models.models import User
from backend.app.services.database import SessionLocal, get_db  # Import from database.py
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/create")
def create_user(db: Session = Depends(get_db)):
    password = "test123"  # Temporary hardcoded password for testing
    hashed = hash_password(password)
    user = User(username="testuser", hashed_password=hashed)
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"message": "User created", "hashed_password": hashed}