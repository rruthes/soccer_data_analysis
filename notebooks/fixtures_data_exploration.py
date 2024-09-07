import requests
import pandas as pd

url = "https://v3.football.api-sports.io/fixtures"

params={
    'league': '71',
    'season': '2022',
}
headers = {
  'x-rapidapi-key': '8d466e7fd56a96fade2767ae8de95e4b',
  'x-rapidapi-host': 'v3.football.api-sports.io'
}

response = requests.request("GET", url, headers=headers, params=params)

df3 = pd.DataFrame(response.json()['response'])
df3.to_csv('fixtures_brasileirao_2024.csv', index=False)
