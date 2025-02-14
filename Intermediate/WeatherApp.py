import requests
from creds import API_KEY2
import json

location = input("Where do you live? \n").capitalize

url = f'https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid={API_KEY2}'

response = requests.get(url)

weather = json.loads(response.text)
print(weather)