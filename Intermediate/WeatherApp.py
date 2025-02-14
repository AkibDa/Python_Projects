import requests
from creds import API_KEY2
import json

location = input("Where do you live? \n").capitalize

url = f'http://api.weatherapi.com/v1/current.json?key=<{API_KEY2}>&q={location}'

response = requests.get(url)

news = json.loads(response.text)
print(news)