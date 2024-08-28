import time
import os
from win32com.client import Dispatch
def water_reminder(interval=10):
    while True:
        print("Time to drink water!")
        if os.name == 'nt':  # For Windows

            speak = Dispatch("SAPI.SpVoice").Speak

            speak("Time to drink water!")
        else:  # For macOS and Linux
            os.system('echo "Time to drink water!"')
        time.sleep(interval)

if __name__ == "__main__":
    reminder_interval = 10  # Set the reminder interval in seconds (3600 seconds = 1 hour)
    water_reminder(reminder_interval)

