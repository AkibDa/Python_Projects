x = [1, 2, 3]
print(dir(x))

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    self.version = 1

p = Person("John", 30)
print(p.__dict__)

# print(help(Person))

class ParentClass:

  def parent_method(self):
    print("This is the parent method.")

class ChildClass(ParentClass):

  def child_method(self):
    print("This is the child method. ")
    super().parent_method()

child_object = ChildClass()
child_object.child_method()