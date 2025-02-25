from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from sqlalchemy.ext.declarative import declarative_base

from alembic import context

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Set up a base for declarative models (update later with actual models)
target_metadata = declarative_base().metadata

def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    raise NotImplementedError("Offline mode not supported yet")
else:
    run_migrations_online()