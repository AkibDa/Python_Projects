class Employee:
  
  def __init__(self, name):
    self.name = name

  def __len__(self):
    i = 0
    for c in self.name:
      i = i + 1
    return i
  
  def __str__(self):
    return(f"The name of the employee is {self.name}")
  
  def __repr__(self):
    return f"Employee('{self.name}')"
  
  def __call__(self):
    print("Hey I am good")

e = Employee('Akib')
print(len(e))
print(str(e))
print(repr(e))

class Shape:

  def __init__(self, x, y):
    self.x = x
    self.y = y

  def area(self):
    return self.x * self.y
  
class Circle(Shape):
  def __init__(self, radius):
    self.radius = radius

  def area(self):
    return 3.24 * self.radius * self.radius

rec = Shape(3, 5)
print(rec.area())

c = Circle(5)
print(c.area())