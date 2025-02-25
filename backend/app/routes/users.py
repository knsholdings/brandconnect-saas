from fastapi import APIRouter
from backend.app.services.auth import hash_password
from backend.app.models.models import UserSchema

router = APIRouter()

@router.post("/create")
def create_user():
    password = "test123"  # Temporary hardcoded password for testing
    hashed = hash_password(password)
    return {"message": "User created", "hashed_password": hashed}