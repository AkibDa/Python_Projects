class Person:
  name = "Akib"
  occupation = "Software Developer"
  networth = 10
  def info(self):
    print(f"{self.name} is a {self.occupation}")

a = Person()
# a.name = 'Shubham'
# a.occupation = 'Accountant'
a.info()

class Details:
  name = "Akib"
  age = "18"
  def show(self):
    print(f"{self.name} is {self.age} years old")

b = Details()
b.show()

class Girl:
  def __init__(self, n, o):
    print("Hey I am a Girl")
    self.name = n
    self.occ = o

  def info(self):
    print(f"{self.name} is a {self.occ}")

c = Girl("Shail","Designer")
c.info()

def greet(fx):
  def mfx():
    print("Good Morning")
    fx()
    print("Thanks for using this function")
  return mfx

@greet
def hello():
  print("Hello World")

hello()