import os
import subprocess
from config import *

backup_file = input("Enter backup file path: ")

command = [
    "pg_restore",
    "-h", DB_HOST,
    "-p", DB_PORT,
    "-U", DB_USER,
    "-d", DB_NAME,
    "-v",
    backup_file
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

    if result.returncode == 0:
        print("Database restored successfully")
    else:
        print("Restore failed")
        print(result.stderr)

except Exception as e:
    print("Error:", e)