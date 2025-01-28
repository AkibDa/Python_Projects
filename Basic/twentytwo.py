class Math:
  def __init__(self, num):
    self.num = num

  def addtonum(self,n):
    self.num = self.num + n

  @staticmethod
  def add(a, b):
    return a + b
  
# result = Math.add(1, 2)
# print(result)

a = Math(5)
print(a.num)
a.addtonum(6)
print(a.num)

print(a.add(7, 2))

class MyClass:
  class_variable = 0

  def __init__(self):
    MyClass.class_variable += 1

  def print_class_variable(self):
    print(MyClass.class_variable)

obj1 = MyClass()
obj2 = MyClass()

obj1.print_class_variable()
obj2.print_class_variable()

class Employee:
  def __init__(self,name):
    self.name = name

  def shoeDetails(self):
    print(f"The name of the employee is {self.name}")

emp1 = Employee("Akib")
# emp1.shoeDetails()
Employee.shoeDetails(emp1)