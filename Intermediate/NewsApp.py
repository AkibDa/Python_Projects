import requests
from env.creds import API_KEY1
import json

query = input("What type of news are you interested in? ")

url = f'https://newsapi.org/v2/everything?q={query}&from=2025-01-01&sortBy=publishedAt&apiKey={API_KEY1}'

response = requests.get(url)

news = json.loads(response.text)
# print(news, type(news))

for article in news["articles"]:
  print("Title:",article["title"])
  print("Desc:",article["description"])
  print("------------------------------------------")