from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.app.models.models import Base
import os

# Use DATABASE_URL for Heroku, fallback to local for development
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+psycopg2://postgres:password@localhost/brandconnect_db")
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True, pool_pre_ping=True)  # Enable echo for debugging, pool_pre_ping for connection health

# Create tables if they don't exist
Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()