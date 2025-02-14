import os
import time

Repeat_Interval = 3600 #Repeat frequency in seconds

while True:
  command = "osascript -e \'say \"Hello Akib Drink Water\"\'; osascript -e \'display alert \"Hey Akib, Drink Water\"\'"

  os.system(command)
  time.sleep(Repeat_Interval)
