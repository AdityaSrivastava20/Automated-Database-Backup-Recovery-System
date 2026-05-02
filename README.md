# Automated-Database-Backup-Recovery-System

# 💾 Automated Database Backup & Recovery System

<p align="center">
  <img src="https://img.shields.io/badge/PostgreSQL-Database-blue?logo=postgresql">
  <img src="https://img.shields.io/badge/Bash-Automation-green?logo=gnubash">
  <img src="https://img.shields.io/badge/Linux-Cron%20Jobs-orange?logo=linux">
  <img src="https://img.shields.io/badge/Python-Optional-yellow?logo=python">
  <img src="https://img.shields.io/badge/Status-Completed-brightgreen">
</p>

---

## 🚀 Overview

This project implements an automated database backup and recovery system using PostgreSQL, Bash scripting, and cron jobs. It simulates real-world DBA tasks such as scheduled backups, data restoration, and system reliability.

---

## 🎯 Objectives

* Automate database backups
* Store timestamped backup files
* Restore database from backup
* Ensure data reliability and recovery

---

## 🧰 Tech Stack

* PostgreSQL
* Bash Scripting
* Linux (cron jobs)
* Python (optional automation)

---

## 🏗️ Project Structure

```id="yhzl9h"
db-backup-system/
│
├── scripts/
│   ├── backup.sh
│   ├── restore.sh
│   └── backup.py
│
├── backups/
│   ├── db_backup_YYYY-MM-DD_HH-MM-SS.sql
│
├── logs/
│   └── backup.log
│
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Configure Backup Script

Edit `backup.sh`:

```bash id="k1qj6p"
DB_NAME="ecommerce"
USER="postgres"
BACKUP_DIR="/home/backup"
```

---

### 2️⃣ Backup Script

```bash id="6bwxqp"
#!/bin/bash

DB_NAME="ecommerce"
USER="postgres"
BACKUP_DIR="/home/backup"

DATE=$(date +%Y-%m-%d_%H-%M-%S)

pg_dump -U $USER $DB_NAME > $BACKUP_DIR/db_backup_$DATE.sql

echo "Backup completed at $DATE"
```

---

### 3️⃣ Make Script Executable

```bash id="g9b5hm"
chmod +x scripts/backup.sh
```

---

### 4️⃣ Schedule Backup (Cron Job)

```bash id="o1qdsj"
crontab -e
```

Add:

```bash id="qv1ndk"
0 2 * * * /path/to/scripts/backup.sh >> /path/to/logs/backup.log 2>&1
```

👉 Runs daily at 2 AM

---

## 🔄 Restore Database

### Restore Script

```bash id="2m2y7r"
#!/bin/bash

DB_NAME="ecommerce"
USER="postgres"
BACKUP_FILE=$1

psql -U $USER $DB_NAME < $BACKUP_FILE

echo "Restore completed"
```

### Run Restore

```bash id="c8v2x6"
./scripts/restore.sh db_backup_2026-05-02_02-00-00.sql
```

---

## 🐍 Optional Python Automation

```python id="6d8p9w"
import os
from datetime import datetime

db_name = "ecommerce"
backup_dir = "/home/backup"

date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

command = f"pg_dump -U postgres {db_name} > {backup_dir}/backup_{date}.sql"

os.system(command)

print("Backup Done")
```

---

## 📸 Screenshots

### ⏰ Cron Job Setup

<p align="center">
  <img src="logs/cron_setup.png" width="700">
</p>

### 💾 Backup Execution

<p align="center">
  <img src="backups/backup_created.png" width="700">
</p>

### 🔄 Restore Execution

<p align="center">
  <img src="backups/restore_process.png" width="700">
</p>

---

## 📊 Features

* Automated database backups
* Timestamp-based file naming
* Restore functionality
* Logging support for monitoring

---

## 📈 Key Learnings

* Database backup strategies using `pg_dump`
* Linux automation using cron jobs
* Restore and recovery techniques
* Basic DBA operational workflows

---

## 📝 Resume Highlights

* Built automated backup system using Bash and cron scheduling
* Implemented database recovery using PostgreSQL tools
* Managed backup storage and logging for reliability

---

## 🚀 Future Improvements

* Cloud backup integration (AWS S3)
* Incremental backups
* Alert system (email notifications)
* Monitoring dashboard

---

## 👨‍💻 Author

**Aditya Srivastava**
📧 [adityasri277@gmail.com](mailto:adityasri277@gmail.com)
🔗 LinkedIn: linkedin.com
💻 GitHub: github.com

---

## ⭐ If you found this useful

Give this repo a star ⭐

