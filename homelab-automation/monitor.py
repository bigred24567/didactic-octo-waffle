import psutil
import time
from datetime import datetime

def log_stats():
  cpu = psutil.cpu_percent()
  mem = psutil.cirtual_memory().percent
  timestamp = datetime.now().isoformat()

  with open("system_log.txt", "a") as f:
    f.write(f"{timestamp}, CPU: {cpu}%, MEM: {mem}%\n")

if __name__ == "__main__":
  while True:
    log_stats)_
    time.sleep(5)
