from functools import reduce

# def double(x):
#   return x * 2

double = lambda x: x * 2
cube = lambda x: x * x * x
avg = lambda x, y, z: (x + y + z) / 3

print(double(5))
print(cube(3))
print(avg(3,6,9))

l = [1,2,4,6,4,3]
newl = list(map(cube, l))
print(newl)

def filter_function(a):
  return a>2

newnewl = list(filter(filter_function, l))
print(newnewl)

numbers = [1, 2, 3, 4, 5]
sum = reduce(lambda x, y: x + y,numbers)
print(sum)

a = "hello"
b = "hello"

print(a == b)
print(a is b)

a = 5
b = 5

print(a == b) # value
print(a is b) # exact location of object in memory