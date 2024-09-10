import requests
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

URL = "https://v3.football.api-sports.io/players"

api_key = os.getenv('API_KEY')

headers = {
  'x-rapidapi-key': api_key,
  'x-rapidapi-host': 'v3.football.api-sports.io'
}

params = {
    'league': '1',
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

df = pd.json_normalize(all_players)
df.to_csv('players_wc_wrong.csv', index=False)

df = pd.read_csv('players_wc_wrong.csv')

df = df.drop(columns=['statistics'])

df.to_csv('players_wc.csv', index=False)