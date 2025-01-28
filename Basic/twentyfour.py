class Employee:

  company = "Apple"

  def __init__(self, name, salary):
    self.name = name
    self.salary = salary

  @classmethod
  def fromStr(cls, string):
    return cls(string.split("-")[0],int(string.split("-")[1]))

  def show(self):
    print(f"The name is {self.name} and company is {self.company}, he earns Rs {self.salary}")

  def changeCompany(cls, newCompany):
    cls.company = newCompany

string = "Akib-12000"
e1 = Employee.fromStr(string)

# e1.name = "Akib"
e1.show()
# e1.changeCompany("Tesla")
# e1.show()

class Person:

  def __init__(self, name, age):
    self.name = name
    self.age = age

  @classmethod
  def from_string (cls,string):
    name, age = string.split(",")
    return cls(name, int(age))
  
person = Person.from_string("John Doe, 30")
print(person.name, person.age)