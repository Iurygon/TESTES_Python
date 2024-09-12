import requests #BIBLIOTECA HTTP PARA FAZER USO DE API

url         = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
response    = requests.get(url)     #ENVIA UMA REQUISIÇÃO DE GET PARA O SERVIDOR

print(response)