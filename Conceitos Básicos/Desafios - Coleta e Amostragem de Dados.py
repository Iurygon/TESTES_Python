#Crie um programa que solicite à pessoa usuária digitar seu nome, e imprima “Olá, [nome]!”.

#Aqui, foram usadas as três maneiras de se adicionar valores não textuais em uma string, o que é chamado de format string
nome = input('Digite seu nome: ')
print(f'Olá, {nome}!') 
print('Olá, %s!' %(nome))
print('Olá, {}!'.format(nome))

#Crie um programa que solicite à pessoa usuária digitar seu nome e idade, e imprima “Olá, [nome], você tem [idade] anos.”.

nome = input('Digite seu nome:')
idade = int(input('Digite sua idade:'))
print('O usuário {} tem {} anos'.format(nome, idade))


#Crie um programa que solicite à pessoa usuária digitar seu nome, idade e altura em metros, e imprima “Olá, [nome], você tem [idade] anos e mede [altura] metros!”.


nome = input('Digite seu nome:')
idade = int(input('Digite sua idade:'))
altura = float(input('Digite sua altura:'))
print('O usuário %s tem %d anos e %.2f de altura' %(nome, idade, altura))

#Crie um programa que solicite dois valores numéricos à pessoa usuária e imprima a soma dos dois valores.

numA = float(input('Digite um número:'))
numB = float(input('Digite um outro número:'))
print(f'A soma dos dois números é {numA + numB}')

#Crie um programa que solicite dois valores numéricos, um numerador e um denominador, e realize a divisão entre os dois valores. Deixe claro que o valor do denominador não pode ser `0`.

numA = float(input('Digite um número para ser dividido:'))
numB = float(input('Digite um outro divisor, diferente de 0:'))
if (numB == 0):
    print('Valor inválido, tente novamente')
else:
    print(f'A soma dos dois números é {numA // numB}')