#Understanding diff type of loops
print("Using loops\n")

name = 'Abhishek'
for i in name:
  print(i,end=",")

colors = ["Red","Green","Blue","Yellow"]
for color in colors:
  print("\n"+color)

for k in range(5):
  print(k+1)

for k in range(1,9):
  print(k)

i=0
while(i<3):
  print(i)
  i=i+1

for i in range(12):
  if(i==10):
    break
  print("5 X",i+1,"=",5 * (i+1))

for i in range(5):
  print(i)
else:
  print("Sorry no i")

for x in range(5):
  print("iteration no {} in for loop".format(x+1))
else:
  print("else block in loop")
print("Out of loop")

fruits = ['apple','banna','mango']
for index, fruit in enumerate(fruits):
  print(index, fruit)

marks = [12,56,32,98,12,45,1,4]

# index = 0
# for mark in marks:
#   print(mark)
#   if(index == 3):
#     print("Harry, awesome!")
#   index += 1

for index, mark in enumerate(marks):
  print(mark)
  if(index == 3):
    print("Harry, awesome!")