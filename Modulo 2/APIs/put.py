import requests

id = 3

url = f"https://68641b8088359a373e978349.mockapi.io/produto/{id}"

data = { 
    "marca":"Gabyy",
    "tamanho":"PP",
    "preco":190.90
}

response = requests.put(url,json=data)

print(response.status_code)
print(response.text)

