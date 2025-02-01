import requests
import creds

url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={creds.API_KEY}'

response = requests.get(url)

print(response.json())