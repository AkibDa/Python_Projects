def factorial(num):
  if(num == 1 or num == 0):
    return 1
  else:
    return (num * factorial(num - 1))
  
num = int(input("Enter any number: "));
print("Number:",num)
print("Factorial of",num,"is:",factorial(num))