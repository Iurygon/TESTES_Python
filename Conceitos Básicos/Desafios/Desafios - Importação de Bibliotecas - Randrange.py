'''
PROGRAMA QUE GERE UM TOKEN DE ACESSO QUE SEJA PAR, ENTRE 1000 E 9998
'''

from random import randrange
'''
RANDRANGE IRÁ SELECIONAR O VALOR ALEATÓRIO ENTRE UM DETERMINADO INTERVALO DE VALORES INTEIROS, PODENDO SER INFORMANDO O 'PASSO' ENTRE CADA VALOR
'''
nome = input('Digite o nome do seu usuário:')

token = randrange(1000, 9998, 2)

print(f'Seja bem vindo, {nome}! Seu token de acesso é {token}.')

