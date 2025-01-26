import math
import os

if(not os.path.exists("data")):
  os.mkdir("data")

# for i in range(0,100):
#   os.mkdir(f"data/Day{i+1}")

try:
  num = int(input("Enter any number: "))
  result = math.sqrt(num)
  print(result)
except:
  print("Invalid Input")
finally:
  print(dir(math))

def main():
  print('Running script directly')

if __name__ == "__main__":
  main()