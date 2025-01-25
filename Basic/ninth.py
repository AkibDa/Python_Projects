#Learning tuples
#Tuples are immutable

tup = (1,2,76,342,32,"green",True)
print(tup,type(tup))
print(len(tup))
print(tup[-1])

if 342 in tup:
  print("Yes")
else:
  print("No")

tup2 = tup[1:4]
print(tup2)

countries = ("Spain","Italy","India","England","Germany")
print(countries)
temp = list(countries)
temp.append("Russia")
temp.pop(3)
temp[2]="Finland"
countries=tuple(temp)
print(countries)

tuple1 = (0,1,2,3,2,31,1,3,2,3)
res = tuple1.index(3)
print("Count of 3 in tuple1 is:",res)