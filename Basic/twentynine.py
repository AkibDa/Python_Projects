class Animal:

  def __init__(self, name, species):
    self.name = name
    self.species = species

  def show_details(self):
    print(f"Name: {self.name}")
    print(f"Species: {self.species}")

class Dog(Animal):
  def __init__(self, name, breed):
    Animal.__init__(self, name, species="Dog")
    self.breed = breed

  def show_details(self):
    Animal.show_details(self)
    print(f"Breed: {self.breed}")

class GoldenRetriver(Dog):
  def __init__(self, name, color):
    Dog.__init__(self, name, breed="Golden Retriver")
    self.color = color

  def show_details(self):
    Dog.show_details(self)
    print(f"Color: {self.color}")

d = GoldenRetriver("Tommy","Black")
d.show_details()

class Employee:
  
  def __init__(self, name):
    self.name = name

  def show(self):
    print(f"The name is {self.name}")

class Dancer:

  def __init__(self, dance):
    self.dance = dance

  def show(self):
    print(f"The dance is {self.dance}")

class DancerEmployee(Employee, Dancer):
  def __init__(self, name, dance):
    self.name = name
    self.dance = dance

o = DancerEmployee("Shivani","Kathak")
print(o.name)
print(o.dance)
o.show()
print(DancerEmployee.mro())

