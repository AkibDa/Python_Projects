import requests
from bs4 import BeautifulSoup

#For Mac

# from os import system

# names = ["Akib","Rohit","Debom","Barnob","Rishi","Abid","Mahroof"]

# for name in names:
#   system(f'say {name}')

# response = requests.get("https://www.google.come")
# print(response.text)

# url = "https://jsonplaceholder.typicode.com/posts"

# data = {
#   "title": 'Akib',
#   "body": 'Da',
#   "userId": 12
# }

# headers = {
#   'Content-type' : 'application/json;charset=UTF-8',
# }

# response = requests.post(url, headers=headers,json=data)

url = "https://www.codewithharry.com/blogpost/django-cheatsheet/"
r = requests.get(url)
# print(r.text)

soup = BeautifulSoup(r.text,'html.parser')

for heading in soup.find_all("h2"):
  print(heading.text)