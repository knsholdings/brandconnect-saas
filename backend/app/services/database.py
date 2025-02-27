from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.app.models.models import Base
import os

# Get the Heroku DATABASE_URL from environment variables and transform for SQLAlchemy
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is not set. Required for Heroku deployment.")
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL, echo=True, pool_pre_ping=True, connect_args={"sslmode": "require"})  # Add SSL for Heroku

# Create tables if they don't exist
Base.metadata.create_all(bind=engine)

# Create a configured session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()