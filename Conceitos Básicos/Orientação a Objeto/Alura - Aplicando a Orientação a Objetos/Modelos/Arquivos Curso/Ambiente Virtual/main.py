import requests
from fastapi import FastAPI, Query #FRAMEWORK USADO PARA FAZER A CRIAÇÃO DO ENDPOINT

#ALÉM DISSO, FOI FEITA A CRIAÇÃO DO SERVIDOR ONDE SERÁ DISPONIBILIZADA A API LOCALMENTE ATRAVÉS DA INSTALAÇÃO DO PACOTE DO UVICORN E INICIADO O SERVIDOR 
#COM O COMANDO 'uvicorn main:app --reload' 

app = FastAPI()   #DEFINE A VARIÁVEL COMO UM OBJETO DA CLASSE 'FastAPI', QUE PERMITE A CRIAÇÃO DO ENDPOINT  

@app.get('/api/hello') #DEFINE O CAMINHO DE OPERAÇÃO DO ENDPOINT
def helloWordl():
    return {'Hello': 'World'}

@app.get('/api/restaurantes/')
def getRestaurantes(restaurante: str = Query(None)):
    url         = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response    = requests.get(url) 

    if response.status_code == 200:
        dadosJson = response.json() #RETORNA, SE HOUVER, A RESPOSTA JSON DO ENDPOINT
        if restaurante == None:
            return {'Dados': dadosJson} #SE NENHUM RESTAURANTE ESPECÍFICO FOR PASSADO, ENTÃO O RESULTADO SERÁ A INFORMAÇÃO DE TODOS ELES
        
        dadosRestaurantes = {}
        for item in dadosJson:
            if item['Company'] == restaurante:
                dadosRestaurantes = []
                dadosRestaurantes.append({  'item': item['Item'],
                                            'price': item['price'],
                                            'description': item['description']
                                            })
        return {'Restaurante': restaurante, 'Cardapio': dadosRestaurantes}
    else:
        print(f'O código do erro foi {response.status_code}')