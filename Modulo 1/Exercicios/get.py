import requests

url = "https://68641b8088359a373e978349.mockapi.io/produto"

reponse = requests.get(url)
print(reponse)
print(reponse.text)