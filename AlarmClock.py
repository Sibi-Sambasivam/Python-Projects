import time
import winsound

def alarm_timer(duration):
    time.sleep(duration)
    frequency = 2500 
    duration = 1000 
    winsound.Beep(frequency, duration)

seconds = int(input("Enter the number of seconds to set the alarm: "))
print(f"Alarm will sound after {seconds} seconds.")
alarm_timer(seconds)
