#Understanding concepts of lists

lst = [11,45,3,5,6]
print(lst)
print(type(lst))
print(lst[0])

if 6 in lst:
  print("Yes")
else:
  print("No")

print(lst[:])

lst.append(7)
print(lst)

lst.sort()
print(lst)

m=lst.copy()
m[0]=0
print(m)
print(lst)

lst.insert(1,899)
print(lst)
lst.sort(reverse=True)
print(lst)

n = [900,1000,1100]
lst.extend(n)
print(lst)
lst.sort(reverse=True)
print(lst)