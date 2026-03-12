import shutil
import os

THRESHOLD = 80  # percent
TARGET_DIR = "/tmp/cleanup"

def check_disk():
  usage = shutil.disk_usage("/")
  percent = (usage.used / usage.total) * 100
  return percent

def cleanup():
  if os.path.exists(TARGET_DIR):
    for file in os.listdir(TARGET_DIR):
      path = os.path.join(TARGET_DIR, file)
      os.remove(path)
    print("Cleanup complete.")

if __name__ == "__main__":
  disk = check_disk()
  if disk > THRESHOLD:
    print("Disk usage high - running cleanup.")
    cleanup()
  else:
    print("Disk usage normal.")
