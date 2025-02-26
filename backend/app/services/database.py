from sqlalchemy.orm import Session
from . import engine  # Assuming engine is defined in database.py

def get_db():
    db = Session(bind=engine)
    try:
        yield db
    finally:
        db.close()