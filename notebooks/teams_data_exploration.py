import requests
import pandas as pd

API_KEY = '8d466e7fd56a96fade2767ae8de95e4b'

headers = {
    'x-apisports-key': API_KEY
}

url = 'https://v3.football.api-sports.io/teams'
params = {
    'league': 71,  
    'season': 2022
}

response = requests.get(url, headers=headers, params=params)
teams = response.json()

df = pd.DataFrame(teams['response'])
df.to_csv('teams_brasileirao_2024.csv', index=False)