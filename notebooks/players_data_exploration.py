import requests
import pandas as pd

URL = "https://v3.football.api-sports.io/players"
headers = {
  'x-rapidapi-key': '8d466e7fd56a96fade2767ae8de95e4b',
  'x-rapidapi-host': 'v3.football.api-sports.io'
}

params = {
    'league': '71',
    'season': '2022',
    'page': 1  
}

all_players = []

while True:
    response = requests.get(URL, headers=headers, params=params)
    data = response.json()

    all_players.extend(data['response'])

    if data['paging']['current'] == data['paging']['total']:
        break

#Como o número de dados era muito extenso, foi necessário dividir a coleta em páginas
    params['page'] += 1

df2 = pd.json_normalize(all_players)
df2.to_csv('players_brasileirao_2022.csv', index=False)
