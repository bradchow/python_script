import winsound
import time

frequency = 500  # Set Frequency To 2500 Hertz
duration = 100  # Set Duration To 1000 ms == 1 second

while(1):
  winsound.Beep(frequency, duration)
  winsound.Beep(frequency, duration)
  winsound.Beep(frequency, duration)
  time.sleep(0.5)
  