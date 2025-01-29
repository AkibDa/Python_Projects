numbers = [1, 2, 3, 4, 5]

while(n := len(numbers)) > 0:
  print(numbers.pop())

a = True
# print(a = False)    Error will show
print(a := False)

happy = True
print(happy)

print(happy := False)

# foods = list()
# while True:
#   food = input("What food do you like?: ")
#   if food == "quit":
#     break
#   foods.append(food)

foods = list()
while (food := input("What food you like?: ")) != "quit":
  foods.append(food)