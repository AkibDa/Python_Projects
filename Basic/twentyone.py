class MyClass:
  def __init__(self, value):
    self._value = value

  def show(self):
    print(f"Value is {self._value}")

  @property
  def ten_value(self):
    return 10* self._value
  
  @ten_value.setter
  def ten_value(self, new_value):
    self._value = new_value/10
  
obj = MyClass(10)
obj.ten_value = 67
print(obj.ten_value)
obj.show()

class Employee:
  def __init__(self,name,id):
    self.name = name
    self.id = id

  def showDetails(self):
    print(f"The name of Employee: {self.id} is {self.name}")

class Programmer(Employee):
  def showLang(self):
    print("The default language is python")

e1 = Employee("Rohan Das",420)
e1.showDetails()
e2 = Programmer("Sk Akib Ahammed",69)
e2.showDetails()
e2.showLang()