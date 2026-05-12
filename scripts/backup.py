import os
import subprocess
from datetime import datetime
from config import *

# Create folders
os.makedirs(BACKUP_DIR, exist_ok=True)
os.makedirs(LOG_DIR, exist_ok=True)

# Timestamp
current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

backup_file = f"{BACKUP_DIR}/{DB_NAME}_{current_time}.backup"
log_file = f"{LOG_DIR}/backup.log"

command = [
    "pg_dump",
    "-h", DB_HOST,
    "-p", DB_PORT,
    "-U", DB_USER,
    "-F", "c",
    "-b",
    "-v",
    "-f", backup_file,
    DB_NAME
]

try:
    env = os.environ.copy()
    env["PGPASSWORD"] = DB_PASSWORD

    result = subprocess.run(
        command,
        env=env,
        capture_output=True,
        text=True
    )

    with open(log_file, "a") as log:
        log.write(f"\n[{current_time}] Backup Started\n")
        log.write(result.stdout)
        log.write(result.stderr)

    if result.returncode == 0:
        print(f"Backup successful: {backup_file}")
    else:
        print("Backup failed")

except Exception as e:
    print("Error:", e)