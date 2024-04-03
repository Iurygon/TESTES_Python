"""
Escreva um programa que peça dois números inteiros e imprima todos os números inteiros entre eles.
"""

numeroUm = int(input('Digite um número inteiro:'))
numeroDois = int(input('Digite outro número inteiro:'))

if numeroUm <= numeroDois:
    for i in range(numeroUm + 1, numeroDois):
        print(i)
else:
    for i in range(numeroDois + 1, numeroUm):
        print(i)

"""
Escreva um programa para calcular quantos dias levará para a colônia de uma bactéria A ultrapassar ou igualar a colônia de uma bactéria B, com base nas taxas de crescimento de 3% e 1,5% respectivamente. Considere que a colônia A inicia com 4 elementos e a colônia B com 10 elementos.
"""

colA = 4
colB = 10
dia = 1

while colA <= colB:
    colA *= 103/100
    colB *= 101.5/100
    dia += 1

print(f'Em {dia} dias, a quantidade de bactérias da colônia A superou da colônia B, sendo um total de {colA} e {colB} bactérias, respectivamente.')

"""
Para tratar uma quantidade de 15 dados de avaliações de pessoas usuárias de um serviço da empresa, precisamos verificar se as notas são válidas. Então, escreva um programa que vai receber a nota de 0 a 5 de todos os dados e verificar se é um valor válido. Caso seja inserido uma nota acima de 5 ou abaixo de 0, repita até que a pessoa usuária insira um valor válido.
"""

contador = 0
listaNotas = []

while contador < 15:
    nota = int(input('Digite uma nota de 0 a 5:'))
    if nota not in [0, 1, 2, 3, 4, 5]:
        print('Valores inválidos, por favor, insira um valor novamente')
    else:
        listaNotas.append(nota)
        contador += 11

"""
Escreva um programa que gere a tabuada de um número inteiro de 1 a 10, de acordo com a escolha da pessoa usuária. Como exemplo, para o número 2, a tabuada deve ser mostrada no seguinte formato:
```
Tabuada do 2:
2 x 1 = 2
2 x 2 = 4
[...]
2 x 10 = 20
```
"""

numero = int(input('Digite um número para exibir a tabuada:'))

for i in range(1, 11):
    print(f'{numero} x {i} = {numero * i}')

"""
Em uma eleição para gerência em uma empresa com 20 funcionários, existem quatro candidatos. Escreva um programa que calcule o vencedor da eleição. A votação ocorreu da seguinte maneira:
- Cada funcionário votou em um dos quatro candidatos (representados pelos números 1, 2, 3 e 4).
- Também foram contabilizados os votos nulos (representado pelo número 5) e os votos em branco (representado pelo número 6).

Ao final da votação, o programa deve exibir o total de votos para cada candidato, o número de votos nulos e o número de votos em branco. Além disso, deve calcular e exibir a porcentagem de votos nulos em relação ao total de votos e a porcentagem de votos em branco em relação ao total de votos.
"""

listVotos = []
votosA = 0
votosB = 0
votosC = 0
votosD = 0
votosNulo = 0
votosBranco = 0

for i in range(1, 21):
    voto = int(input('Digite seu candidato para o voto:'))
    listVotos.append(voto)

votosA = listVotos.count(1)
votosB = listVotos.count(2)
votosC = listVotos.count(3)
votosD = listVotos.count(4)
votosNulo = listVotos.count(5)
votosBranco = listVotos.count(6)

print(f'A quantidade de votos para o candidato A foi de {votosA}, {(votosA * 100) / 20}% comparado ao total')
print(f'A quantidade de votos para o candidato B foi de {votosB}, {(votosB * 100) / 20}% comparado ao total')
print(f'A quantidade de votos para o candidato C foi de {votosC}, {(votosC * 100) / 20}% comparado ao total')
print(f'A quantidade de votos para o candidato D foi de {votosD}, {(votosD * 100) / 20}% comparado ao total')
print(f'A quantidade de votos nulos foi de {votosNulo}, {(votosNulo * 100) / 20}% comparado ao total')
print(f'A quantidade de votos brancos foi de {votosBranco}, {(votosBranco * 100) / 20}% comparado ao total')