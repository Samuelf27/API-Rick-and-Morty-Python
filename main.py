import requests

def fetch_data(endpoint, filter={}):
    url = f"https://rickandmortyapi.com/api/{endpoint}"  # Usa o endpoint recebido
    response = requests.get(url, params=filter)
    
    return response.json() if response.status_code == 200 else None

# Busca os dados de personagens
characters = fetch_data("character", {"name": "Rick"})  # Corrigido o uso do filtro
if characters:
    print(characters)
else:
    print('Failed to fetch data')  
