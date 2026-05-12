import os
import time
from config import BACKUP_DIR

DAYS_TO_KEEP = 7

current_time = time.time()

for file in os.listdir(BACKUP_DIR):

    file_path = os.path.join(BACKUP_DIR, file)

    if os.path.isfile(file_path):

        file_age = current_time - os.path.getmtime(file_path)

        if file_age > DAYS_TO_KEEP * 86400:
            os.remove(file_path)
            print(f"Deleted old backup: {file}")