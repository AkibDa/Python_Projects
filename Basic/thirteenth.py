'''Sets'''

#sets won't have duplicate items
#sets doesn't follow order

s = {2,4,2,6,2,8,2,10}
print(s)

cities = {"Tokyo","Madrid","Berlin","Delhi"}
cities2 = {"Tokyo","Seoul","Kabul","Madrid"}
cities3 = cities.union(cities2)
print(cities3)
cities4 = cities.intersection(cities2)
print(cities4)
cities5 = cities.symmetric_difference(cities2)
print(cities5)

s1 = {1,2,5,6}
s2 = {3,6,7}
s1.update(s2)
print(s1,s2)

'''Dictionaries'''

info = {"name":"Karan","age":19,"eligible":True}
print(info["name"])
print(info.get("eligible"))

for key in info.keys():
  print(f"The value corresponding to the key {key} is {info[key]}")

info.update({"DOB":2005})
print(info)