
f = open('myfile.txt','r')
# print(f)
text = f.read()
print(text)
f.close()

f = open('myfile.txt','w')
f.write("Helllo World")
f.close()

with open('myfile.txt','a') as f:
  f.write("Hey I am inside with")

f = open('myfile.txt','r')
while True:
  line = f.readline()
  if not line:
    break
  print(line)

f = open('myfile.txt','w')
lines = ['line 1\n','line 2\n','line 3\n']
f.writelines(lines)
f.close

f = open('myfile.txt','w')
lines = ['line 1','line 2','line 3']
for line in lines:
  f.write(line + '\n')
f.close