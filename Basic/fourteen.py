'''Exception Handling'''

a = input("Enter the number: ")
print(f"Multiplicatio table of {a} is: ")

try:
  for i in range(1,11):
    print(f"{int(a)} X {i} = {int(a)*i}")
except:
  print("Invalid Input")

print("Some imp lines of code")
print("End of program")

try:
  num = int(input("Enter an integer: "))
  a = [6,3]
  print(a[num])
except ValueError:
  print("Number entered is not an integer. ")
except IndexError:
  print("Index error")

def func1():
  try:
    l = [1,5,6,7]
    i = int(input("Enter the index: "))
    print(l[i])
    return 1
  except:
    print("Some error occurred")
    return 0
  finally:
    print("I am always executed")

x = func1()
print(x)

b = int(input("Enter any number between 5 and 9 "))

if(a<5 or a>9):
  raise ValueError("Value should be between 5 and 9")

salary = int(input("Enter salary amount: "))
if not 2000 < salary < 5000:
  raise ValueError("Not a valid salary")