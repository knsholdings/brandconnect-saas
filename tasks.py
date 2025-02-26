from datetime import datetime
import os
import subprocess

def backup_database():
    db_url = os.getenv("DATABASE_URL")  # Heroku provides this
    backup_file = f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.sql"
    cmd = f"pg_dump {db_url} > {backup_file}"
    subprocess.run(cmd, shell=True, capture_output=True, text=True)
    subprocess.run(f"heroku ps:restart", shell=True)  # Ensure app restarts cleanly