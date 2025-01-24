a=9
b=8

def calculateGmean(a,b):
  mean = (a*b)/(a+b)
  print(mean)

c=8
d=7

calculateGmean(a,b)
calculateGmean(c,d)

def isGreater(a,b):
  if(a>b):
    print("First number is greater")
  else:
    print("Second number is greater")

isGreater(a,b)
isGreater(c,d)

def isLesser(a,b):
  pass

def average(a,b):
  print("The average is ",(a+b)/2)

average(a,b)

def name(**name):
  print(type(name))
  print("Hello,",name["fname"],name["mname"],name["lname"])

name(mname="Buchanan",lname="Barnes",fname="James")