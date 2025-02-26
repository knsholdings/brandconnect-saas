import os
from sqlalchemy import create_engine

# Get the Heroku DATABASE_URL from environment variables
database_url = os.getenv("DATABASE_URL")

# Replace 'postgres://' with 'postgresql://' for SQLAlchemy compatibility
if database_url and database_url.startswith("postgres://"):
    database_url = database_url.replace("postgres://", "postgresql://", 1)

# Create the SQLAlchemy engine
engine = create_engine(database_url)