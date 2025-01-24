#String are immutable
name = input("Enter your name : ");
print("Lets use for loop\n");
for chr in name :
  print(chr+"\n");
print(len(name));

fruit = input("Enter any fruit : ");
fruitln = len(fruit);
print(fruit[0:4]); #String slicing

#Quick Quiz
# nm = "harry"
# print(nm[-4:-2])

print(name.upper());
print(name.lower());

blogHeading = "hello,hOw are yOu?";
print(blogHeading.capitalize());