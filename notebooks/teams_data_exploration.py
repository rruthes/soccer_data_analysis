import requests
import pandas as pd

url = 'https://v3.football.api-sports.io/teams'  

headers = {
      'x-rapidapi-key': '8d466e7fd56a96fade2767ae8de95e4b',
    'x-rapidapi-host': 'v3.football.api-sports.io'
}

params = {
    'league': 71,
    'season': 2022
}

response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    teams = response.json()

    df = pd.DataFrame(teams['response'])
    df.to_csv('teams_brasileirao_2024.csv', index=False)
else:
    print(f"Failed to retrieve data: {response.status_code}")

data = [
    {'id': 119, 'name': 'Internacional', 'code': 'INT', 'country': 'Brazil', 'founded': 1909, 'national': False, 'logo': 'https://media.api-sports.io/football/teams/119.png', 'stadium_id': 244, 'stadium_name': 'Estádio José Pinheiro Borda', 'stadium_address': 'Avenida Padre Cacique 891, Bairro Menino Deus', 'stadium_city': 'Porto Alegre, Rio Grande do Sul', 'stadium_capacity': 50128, 'stadium_surface': 'grass', 'stadium_image': 'https://media.api-sports.io/football/venues/244.png'},
    {'id': 120, 'name': 'Botafogo', 'code': 'BOT', 'country': 'Brazil', 'founded': 1904, 'national': False, 'logo': 'https://media.api-sports.io/football/teams/120.png', 'stadium_id': 218, 'stadium_name': 'Estádio Nilton Santos', 'stadium_address': 'Rua Arquias Cordeiro, Engenho de Dentro', 'stadium_city': 'Rio de Janeiro', 'stadium_capacity': 46931, 'stadium_surface': 'grass', 'stadium_image': 'https://media.api-sports.io/football/venues/218.png'},
    {'id': 121, 'name': 'Palmeiras', 'code': 'PAL', 'country': 'Brazil', 'founded': 1914, 'national': False, 'logo': 'https://media.api-sports.io/football/teams/121.png', 'stadium_id': 258, 'stadium_name': 'Allianz Parque', 'stadium_address': 'Rua Turiaçu 1840, Perdizes', 'stadium_city': 'São Paulo, São Paulo', 'stadium_capacity': 43713, 'stadium_surface': 'grass', 'stadium_image': 'https://media.api-sports.io/football/venues/258.png'},
    {'id': 124, 'name': 'Fluminense', 'code': 'FLU', 'country': 'Brazil', 'founded': 1902, 'national': False, 'logo': 'https://media.api-sports.io/football/teams/124.png', 'stadium_id': 204, 'stadium_name': 'Estadio Jornalista Mário Filho (Maracanã)', 'stadium_address': 'Rua Professor Eurico Rabelo, Maracanã', 'stadium_city': 'Rio de Janeiro, Rio de Janeiro', 'stadium_capacity': 78838, 'stadium_surface': 'grass', 'stadium_image': 'https://media.api-sports.io/football/venues/204.png'},
    {'id': 125, 'name': 'America Mineiro', 'code': 'AME', 'country': 'Brazil', 'founded': 1912, 'national': False, 'logo': 'https://media.api-sports.io/football/teams/125.png', 'stadium_id': 206, 'stadium_name': 'Estádio Raimundo Sampaio', 'stadium_address': 'Avenida Ismênia Tunes, Bairro Horto', 'stadium_city': 'Belo Horizonte, Minas Gerais', 'stadium_capacity': 23018, 'stadium_surface': 'grass', 'stadium_image': 'https://media.api-sports.io/football/venues/206.png'},
    {'id': 126, 'name': 'Sao Paulo', 'code': 'PAU', 'country': 'Brazil', 'founded': 1930, 'national': False, 'logo': 'https://media.api-sports.io/football/teams/126.png', 'stadium_id': 269, 'stadium_name': 'Estádio Cícero Pompeu de Toledo (Morumbi)', 'stadium_address': 'Praca Roberto Gomes Pedrosa 1, Morumbi', 'stadium_city': 'São Paulo, São Paulo', 'stadium_capacity': 66795, 'stadium_surface': 'grass', 'stadium_image': 'https://media.api-sports.io/football/venues/269.png'},
    {'id': 127, 'name': 'Flamengo', 'code': 'FLA', 'country': 'Brazil', 'founded': 1895, 'national': False, 'logo': 'https://media.api-sports.io/football/teams/127.png', 'stadium_id': 204, 'stadium_name': 'Estadio Jornalista Mário Filho (Maracanã)', 'stadium_address': 'Rua Professor Eurico Rabelo, Maracanã', 'stadium_city': 'Rio de Janeiro, Rio de Janeiro', 'stadium_capacity': 78838, 'stadium_surface': 'grass', 'stadium_image': 'https://media.api-sports.io/football/venues/204.png'},
    {'id': 128, 'name': 'Santos', 'code': 'SAN', 'country': 'Brazil', 'founded': 1912, 'national': False, 'logo': 'https://media.api-sports.io/football/teams/128.png', 'stadium_id': 10494, 'stadium_name': 'Estádio Urbano Caldeira', 'stadium_address': 'Rue Princesa Isabel 77, Vila Belmiro', 'stadium_city': 'Santos, São Paulo', 'stadium_capacity': 21256, 'stadium_surface': 'grass', 'stadium_image': 'https://media.api-sports.io/football/venues/10494.png'},
    {'id': 129, 'name': 'Ceara', 'code': 'CEA', 'country': 'Brazil', 'founded': 1914, 'national': False, 'logo': 'https://media.api-sports.io/football/teams/129.png', 'stadium_id': 225, 'stadium_name': 'Estádio Governador Plácido Aderaldo Castelo', 'stadium_address': 'Avenida Alberto Craveiro, Passaré', 'stadium_city': 'Fortaleza, Ceará', 'stadium_capacity': 63903, 'stadium_surface': 'grass', 'stadium_image': 'https://media.api-sports.io/football/venues/225.png'},
    {'id': 131, 'name': 'Corinthians', 'code': 'COR', 'country': 'Brazil', 'founded': 1910, 'national': False, 'logo': 'https://media.api-sports.io/football/teams/131.png', 'stadium_id': 11531, 'stadium_name': 'Neo Química Arena', 'stadium_address': 'Avenida Miguel Inácio Curi, 111, Vila Carmosina, Itaquera', 'stadium_city': 'São Paulo, São Paulo', 'stadium_capacity': 49205, 'stadium_surface': 'grass', 'stadium_image': 'https://media.api-sports.io/football/venues/11531.png'},
    {'id': 134, 'name': 'Atletico Paranaense', 'code': 'ATL', 'country': 'Brazil', 'founded': 1924, 'national': False, 'logo': 'https://media.api-sports.io/football/teams/134.png', 'stadium_id': 10493, 'stadium_name': 'Arena da Baixada', 'stadium_address': 'Rua Buenos Aires 1260, Água Verde', 'stadium_city': 'Curitiba, Paraná', 'stadium_capacity': 43981, 'stadium_surface': 'grass', 'stadium_image': 'https://media.api-sports.io/football/venues/10493.png'},
    {'id': 144, 'name': 'Atletico Goianiense', 'code': 'ATL', 'country': 'Brazil', 'founded': 1937, 'national': False, 'logo': 'https://media.api-sports.io/football/teams/144.png', 'stadium_id': 211, 'stadium_name': 'Estádio Antônio Accioly', 'stadium_address': 'Avenida Perimetral 923 / Avenida 24 de Outubro, Bairro Campinas', 'stadium_city': 'Goiânia, Goiás', 'stadium_capacity': 12500, 'stadium_surface': 'grass', 'stadium_image': 'https://media.api-sports.io/football/venues/211.png'},
    {'id': 145, 'name': 'Avai', 'code': 'AVA', 'country': 'Brazil', 'founded': 1923, 'national': False, 'logo': 'https://media.api-sports.io/football/teams/145.png', 'stadium_id': 214, 'stadium_name': 'Estádio Aderbal Ramos da Silva', 'stadium_address': 'Avenida Deputado Diomício Freitas 1000, Bairro Carianos', 'stadium_city': 'Florianópolis, Santa Catarina', 'stadium_capacity': 19000, 'stadium_surface': 'grass', 'stadium_image': 'https://media.api-sports.io/football/venues/214.png'},
    {'id': 147, 'name': 'Coritiba', 'code': 'COR', 'country': 'Brazil', 'founded': 1909, 'national': False, 'logo': 'https://media.api-sports.io/football/teams/147.png', 'stadium_id': 230, 'stadium_name': 'Estádio Major Antônio Couto Pereira', 'stadium_address': 'Rua Ubaldino do Amaral 37, Bairro Alto da Glória', 'stadium_city': 'Curitiba, Paraná', 'stadium_capacity': 45563, 'stadium_surface': 'grass', 'stadium_image': 'https://media.api-sports.io/football/venues/230.png'},
    {'id': 151, 'name': 'Goias', 'code': 'GOI', 'country': 'Brazil', 'founded': 1943, 'national': False, 'logo': 'https://media.api-sports.io/football/teams/151.png', 'stadium_id': 240, 'stadium_name': 'Estádio de Hailé Pinheiro', 'stadium_address': 'Avenida Edmundo Pinheiro de Abreu 721, Setor Bela Vista', 'stadium_city': 'Goiânia, Goiás', 'stadium_capacity': 14525, 'stadium_surface': 'grass', 'stadium_image': 'https://media.api-sports.io/football/venues/240.png'},
    {'id': 152, 'name': 'Juventude', 'code': 'JUV', 'country': 'Brazil', 'founded': 1913, 'national': False, 'logo': 'https://media.api-sports.io/football/teams/152.png', 'stadium_id': 248, 'stadium_name': 'Estádio Alfredo Jaconi', 'stadium_address': 'Rua Hércules Galló 1547', 'stadium_city': 'Caxias do Sul, Rio Grande do Sul', 'stadium_capacity': 19924, 'stadium_surface': 'grass', 'stadium_image': 'https://media.api-sports.io/football/venues/248.png'},
    {'id': 154, 'name': 'Fortaleza EC', 'code': 'FOR', 'country': 'Brazil', 'founded': 1918, 'national': False, 'logo': 'https://media.api-sports.io/football/teams/154.png', 'stadium_id': 225, 'stadium_name': 'Estádio Governador Plácido Aderaldo Castelo', 'stadium_address': 'Avenida Alberto Craveiro, Passaré', 'stadium_city': 'Fortaleza, Ceará', 'stadium_capacity': 63903, 'stadium_surface': 'grass', 'stadium_image': 'https://media.api-sports.io/football/venues/225.png'},
    {'id': 794, 'name': 'RB Bragantino', 'code': 'BRA', 'country': 'Brazil', 'founded': 1928, 'national': False, 'logo': 'https://media.api-sports.io/football/teams/794.png', 'stadium_id': 220, 'stadium_name': 'Estádio Nabi Abi Chedid', 'stadium_address': 'Rua Emílio Coleta', 'stadium_city': 'Bragança Paulista, São Paulo', 'stadium_capacity': 17128, 'stadium_surface': 'grass', 'stadium_image': 'https://media.api-sports.io/football/venues/220.png'},
    {'id': 1062, 'name': 'Atletico-MG', 'code': 'ATL', 'country': 'Brazil', 'founded': 1908, 'national': False, 'logo': 'https://media.api-sports.io/football/teams/1062.png', 'stadium_id': 206, 'stadium_name': 'Estádio Raimundo Sampaio', 'stadium_address': 'Avenida Ismênia Tunes, Bairro Horto', 'stadium_city': 'Belo Horizonte, Minas Gerais', 'stadium_capacity': 23018, 'stadium_surface': 'grass', 'stadium_image': 'https://media.api-sports.io/football/venues/206.png'},
    {'id': 1193, 'name': 'Cuiaba', 'code': 'CUI', 'country': 'Brazil', 'founded': 2001, 'national': False, 'logo': 'https://media.api-sports.io/football/teams/1193.png', 'stadium_id': 235, 'stadium_name': 'Arena Pantanal', 'stadium_address': None, 'stadium_city': 'Cuiabá, Mato Grosso', 'stadium_capacity': 44003, 'stadium_surface': 'grass', 'stadium_image': 'https://media.api-sports.io/football/venues/235.png'}
]

df_manual = pd.DataFrame(data)

df_manual.to_csv('teams_and_stadiums.csv', index=False)

print(df_manual.head())