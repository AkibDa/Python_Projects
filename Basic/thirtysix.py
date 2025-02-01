import os
import time

timestamp = time.strftime('%H:%M:%S')
print(timestamp);
os.system(f"say The time is {timestamp}")
os.system("say drink some water")

hour = int(time.strftime('%H'))
