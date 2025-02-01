import requests
import creds

url = f'https://newsapi.org/v2/top-headlines?country=in&apiKey={creds.API_KEY}'

response = requests.get(url)

print(response.json())