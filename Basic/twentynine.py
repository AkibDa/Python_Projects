class Animal:

  def __init__(self, name, species):
    self.name = name
    self.species = species

  def make_sound(self):
    print("Sound made by the animal")

class Dog(Animal):
  def __init__(self, name, breed):
    Animal.__init__(self, name, species="Dog")
    self.breed = breed

  def make_sound(self):
    print("Bark!")

d = Dog("Dog","Doggerman")
d.make_sound()

a = Animal("Dog", "Dog")
a.make_sound()

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

