from config.schedule import setup_schedules  
import schedule
import time

print("Setting up schedules...")
setup_schedules()

while True:
    schedule.run_pending()
    time.sleep(1)