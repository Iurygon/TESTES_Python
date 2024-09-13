import requests #BIBLIOTECA HTTP PARA FAZER USO DE API
import json     #BIBLIOTECA PARA TRATAR ARQUIVOS JSON

url         = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
response    = requests.get(url)     #ENVIA UMA REQUISIÇÃO DE GET PARA O ENDPOINT

#print(response) 
#RETORNA UM VALOR QUE CORRESPONDE A RESPOSTA DURANTE A BUSCA NO ENDPOINT. NORMALMENTE, A RESPOSTA PARA UMA BUSCA COM SUCESSO É 200, SENDO ASSIM, PODEMOS FAZER A SEGUINTE VERIFICAÇÃO

if response.status_code == 200:
    dadosJson = response.json() #RETORNA, SE HOUVER, A RESPOSTA JSON DO ENDPOINT
    # print(dadosJson)
    dadosRestaurantes = {}
    for item in dadosJson:
        nomeRestaurante = item['Company']
        if nomeRestaurante not in dadosRestaurantes:
            dadosRestaurantes[nomeRestaurante] = {}
        dadosRestaurantes[nomeRestaurante].append({'item': item['Item'],
                                                    'price': item['price'],
                                                    'description': item['description']
                                                    })
    # print(dadosRestaurantes['McDonald’s'])
else:
    print(f'O código do erro foi {response.status_code}')

for nomeDoRestaurante, dados in dadosRestaurantes.items():
    nomeArquivo = f'{nomeDoRestaurante}.json'
    with open(nomeArquivo, 'w') as arquivosRestaurantes:
        json.dump(dados, arquivosRestaurantes, indent=4)

#WITH OPEN É UM COMANDO PYTHON PARA INTERAGIR COM ARQUIVOS, QUE RECEBE O NOME DO ARQUIVO E O MODO DE INTERAÇÃO (NESSE CASO, 'W' DE 'WRITE'). ASSIM, O QUE SERÁ ESCRITO NO ARQUIVO SERÃO
#OS DADOS DO DICIONÁRIO DE RESTAURANTES, PASSANDO NO FORMATO JSON, COM O COMANDO 'json.dump()'. O COMANDO RECEBE COMO PARÂMETROS OS DADOS QUE SERÃO INSERIDOS, EM QUAL ARQUIVO (QUE NESSE
#CASO, FOI AQUELE CRIADO PELO WITH OPEN) E A IDENTAÇÃO DO ARQUIVO.        
