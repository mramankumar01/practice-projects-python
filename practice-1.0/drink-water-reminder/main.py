import time
from plyer import notification

while True:
    print("Please! Sip some water now! 💧")
    notification.notify(title="Please drink water", message="Its important to stay hydrated!")
    time.sleep(60*60)  # Remind every hour