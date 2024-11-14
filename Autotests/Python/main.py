import requests
URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'c77c3c2af2f88cd7995d7fa92a0bd1b6'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}
body_create = {
    "name": "generate",
    "photo_id": -1
}


response_create = requests.post(url= f'{URL}/pokemons', headers = HEADER, json = body_create)
assert response_create.status_code == 201
print(response_create.text)

pokemon_id = response_create.json()['id']
print(pokemon_id)

body_rename = {
    "pokemon_id": pokemon_id,
    "name": "New Name",
    "photo_id": 2
}

body_pokemon_id = {
    "pokemon_id": pokemon_id
}
response_rename = requests.patch(url= f'{URL}/pokemons', headers = HEADER, json = body_rename)
print(response_rename.text)
assert response_rename.status_code == 200

response_pokeball = requests.post(url= f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokemon_id)
print(response_pokeball.text)
assert response_pokeball.status_code == 200

response_knockout = requests.post(url= f'{URL}/pokemons/knockout', headers = HEADER, json = body_pokemon_id)
print(response_knockout.text)
assert response_knockout.status_code == 200
