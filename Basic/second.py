a=int(input("Enter first number: "));
b=int(input("Enter second number: "));
c=input("Choose a math operationc(+,-,*,/): ")

# ans1 = a+b;
# print("Addition of",a,"and",b,"is equal to",ans1);
# ans2 = a-b;
# print("Substraction of",a,"and",b,"is equal to",ans2);
# ans3 = a*b;
# print("Multiplication of",a,"and",b,"is equal to",ans3);
# ans4 = a/b;
# print("Division of",a,"and",b,"is equal to",ans4);

match c:
  case '+':
    print("Addition of",a,"and",b,"is equal to",a+b);
  case '-':
    print("Substraction of",a,"and",b,"is equal to",a-b);
  case '*':
    print("Multiplication of",a,"and",b,"is equal to",a*b);
  case '/':
    print("Division of",a,"and",b,"is equal to",a/b);
  case _:
    print("Choose a correct operator");
