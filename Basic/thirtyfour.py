import requests
from creds import API_KEY

url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}'

response = requests.get(url)

print(response.json())