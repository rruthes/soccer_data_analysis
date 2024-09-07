import requests
import pandas as pd

url = "https://v3.football.api-sports.io/fixtures"
headers = {
  'x-rapidapi-key': '8d466e7fd56a96fade2767ae8de95e4b',
  'x-rapidapi-host': 'v3.football.api-sports.io'
}

params = {
    'league': '71',
    'season': '2022',
    'page': 1  
}

all_fixtures = []

while True:
    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    all_fixtures.extend(data['response'])

    if data['paging']['current'] == data['paging']['total']:
        break

#Como o número de dados era muito extenso, foi necessário dividir a coleta em páginas
params['page'] += 1

df3 = pd.DataFrame(all_fixtures)

print(df3.head())

df3.to_csv('fixtures_brasileirao_2024.csv', index=False)