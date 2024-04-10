import requests

url_api = "https://api.nasa.gov/planetary/apod?api_key=oC25risdTYrNejPzuR79GXJkNI8ojmFNhieRYLry"

response = requests.get(url_api)

if response.status_code == 200:
    dados = response.json()
    print(dados['url'])
