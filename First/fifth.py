import time

timestamp = time.strftime('%H:%M:%S')
print(timestamp);
timestamp = int(time.strftime('%H'));

if (timestamp < 12):
  print("Good Morning Sir");
elif (timestamp <= 16):
  print("Good Afternoon Sir");
elif (timestamp <= 20):
  print("Good Evening Sir");
else:
  print("Goodnight Sir");