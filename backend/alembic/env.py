import os
from sqlalchemy import create_engine
from alembic import context

# Retrieve DATABASE_URL from environment
database_url = os.getenv("DATABASE_URL")
print("DATABASE_URL from env:", database_url)  # Debug print for verification

# Ensure DATABASE_URL is set; raise an error if not (no local fallback)
if not database_url:
    raise ValueError("DATABASE_URL environment variable is not set. Required for Heroku deployment.")

# Modify for SQLAlchemy compatibility and Heroku requirements
if database_url.startswith("postgres://"):
    database_url = database_url.replace("postgres://", "postgresql://", 1)
if "sslmode" not in database_url:
    database_url += "?sslmode=require"
print("Final DATABASE_URL:", database_url)  # Debug print for verification

# Create SQLAlchemy engine
engine = create_engine(database_url)

# Ensure target_metadata is imported and set
from backend.app.models.models import Base
target_metadata = Base.metadata

# Run migrations
with engine.connect() as connection:
    context.configure(connection=connection, target_metadata=target_metadata)
    with context.begin_transaction():
        context.run_migrations()