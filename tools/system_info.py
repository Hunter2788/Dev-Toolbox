import platform
import psutil

def run():
    print("\n--- SYSTEM INFO ---")
    print(f"System: {platform.system()}")
    print(f"Processor: {platform.processor()}")
    print(f"CPU Usage: {psutil.cpu_percent()}%")
    print(f"RAM Usage: {psutil.virtual_memory().percent}%")
    print(f"Disk Usage: {psutil.disk_usage('/').percent}%")
