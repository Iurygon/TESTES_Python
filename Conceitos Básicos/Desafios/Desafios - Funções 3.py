'''
CRIE UM CÓDIGO QUE UNA OS NOMES E SOBRENOMES DAS LISTAS A SEGUIR NA SEGUINTE FORMATAÇÃO:

Nome Completo: Nome Sobrenome
'''

nomes = ["joão", "MaRia", "JOSÉ"]
sobrenomes = ["SILVA", "souza", "Tavares"]

for nome in nomes:
    for sobrenome in sobrenomes:
        nome.lower()
        sobrenome.lower()
        print(f'{nome.capitalize()} {sobrenome.capitalize()}')