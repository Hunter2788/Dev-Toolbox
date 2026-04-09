import shutil
import os
from datetime import datetime

def run():
    source = input("Source folder: ")
    destination = input("Backup folder: ")

    if not os.path.exists(source):
        print("Source folder not found")
        return

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"backup_{timestamp}"
    backup_path = os.path.join(destination, backup_name)

    try:
        shutil.copytree(source, backup_path)
        print(f"Backup created at {backup_path}")
    except Exception as e:
        print(f"Backup failed: {e}")
