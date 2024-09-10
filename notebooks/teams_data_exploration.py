import requests
import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

URL = 'https://v3.football.api-sports.io/teams'  

api_key = os.getenv('API_KEY')

headers = {
      'x-rapidapi-key': api_key,
      'x-rapidapi-host': 'v3.football.api-sports.io'
}

params = {
    'league': 1,
    'season': 2022
}

response = requests.get(URL, headers=headers, params=params)
data = response.json()
print(data)

all_teams = []

all_teams.extend(data['response'])
df2 = pd.json_normalize(all_teams)
df2.to_csv('teams_wc.csv', index=False)