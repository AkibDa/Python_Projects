letter = "Hey my name is {} and I am from {}"
country = "India"
name = "Akib"

print(letter.format(country,name))
print(f"Hey my name is {name} and I am from {country}")

price = 49.09999
txt = f"For only {price:.2f} dollars!"
print(txt)

print(f"{2*30}")
print(type(f"{2*30}"))

def square(n):
  '''Takes in a number n, returns the square of n'''
  print(n**2)
square(5)
print(square.__doc__)