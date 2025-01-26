#Using if-elif-else statements
a = int(input("Enter your age: "));
print("Your age is:",a);

if(a>18):
  print("You can drive");
else:
  print("You cannot drive");

# print(a>18);
# print(a<=18);
# print(a==18);
# print(a!=18);

applePrice = 10;
budget = 200;

if (budget - applePrice > 50):
  print("Alexa, add 1kg Apples to the cart.")
elif (budget - applePrice > 70):
  print("Its okay you can buy. ")
else :
  print("Alexa, do not add Apples to the cart. ")

num = int(input("Enter any number: "));

if(num > 0):
  print("Number is Positive");
elif(num < 0):
  print("Number is Negative");
else:
  print("Number is Zero");

b = 330
c = 3303

print("B") if b > c else print("=") if c == b else print("C")

d = 9 if b>c else 0
print(d)