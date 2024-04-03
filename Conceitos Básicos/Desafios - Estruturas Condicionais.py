#Um programa deve ser escrito para ler dois números e, em seguida, perguntar à pessoa usuária qual operação ele deseja realizar. O resultado da operação deve incluir informações sobre o número - se é par ou ímpar, positivo ou negativo e inteiro ou decimal.

numeroUm = float(input('Digite um número: '))
numeroDois = float(input('Digite outro:'))
operacao = input('Qual operação será feita: Soma, Subtração, Multiplicação, Divisão')
resultado = 0

if operacao == 'Soma':
    resultado = numeroUm + numeroDois
    print('O resultado da operação {} é {}'.format(operacao, resultado))
    if resultado % 2 == 0:
        print('{} é um número par'.format(resultado))
    else:
        print('{} é um número ímpar'.format(resultado))

    if resultado > 0:
        print('{} é um número positivo'.format(resultado))
    elif resultado < 0:
        print(f'{resultado} é um número negativo')
    else:
        print(f'{resultado} não possui valor')

    if '.0' in str(resultado):
        print(f'{resultado} é um número inteiro')
    else:
        print(f'{resultado} é um número decimal')
elif operacao == 'Subtração':
    resultado = numeroUm - numeroDois
    print('O resultado da operação {} é {}'.format(operacao, resultado))
    if resultado % 2 == 0:
        print('{} é um número par'.format(resultado))
    else:
        print('{} é um número ímpar'.format(resultado))

    if resultado > 0:
        print('{} é um número positivo'.format(resultado))
    elif resultado < 0:
        print(f'{resultado} é um número negativo')
    else:
        print(f'{resultado} não possui valor')

    if '.0' in str(resultado):
        print(f'{resultado} é um número inteiro')
    else:
        print(f'{resultado} é um número decimal')
elif operacao == 'Multiplicação':
    resultado = numeroUm * numeroDois
    print('O resultado da operação {} é {}'.format(operacao, resultado))
    if resultado % 2 == 0:
        print('{} é um número par'.format(resultado))
    else:
        print('{} é um número ímpar'.format(resultado))

    if resultado > 0:
        print('{} é um número positivo'.format(resultado))
    elif resultado < 0:
        print(f'{resultado} é um número negativo')
    else:
        print(f'{resultado} não possui valor')

    if '.0' in str(resultado):
        print(f'{resultado} é um número inteiro')
    else:
        print(f'{resultado} é um número decimal')
elif operacao == 'Divisão':
    resultado = numeroUm / numeroDois
    print('O resultado da operação {} é {}'.format(operacao, resultado))
    if resultado % 2 == 0:
        print('{} é um número par'.format(resultado))
    else:
        print('{} é um número ímpar'.format(resultado))

    if resultado > 0:
        print('{} é um número positivo'.format(resultado))
    elif resultado < 0:
        print(f'{resultado} é um número negativo')
    else:
        print(f'{resultado} não possui valor')

    if '.0' in str(resultado):
        print(f'{resultado} é um número inteiro')
    else:
        print(f'{resultado} é um número decimal')
else:
    print('Operação inválida!')

"""
Escreva um programa que peça à pessoa usuária três números que representam os lados de um triângulo. O programa deve informar se os valores podem ser utilizados para formar um triângulo e, caso afirmativo, se ele é equilátero, isósceles ou escaleno. Tenha em mente algumas dicas:
- Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
- Triângulo Equilátero: três lados iguais;
- Triângulo Isósceles: quaisquer dois lados iguais;
- Triângulo Escaleno: três lados diferentes;
"""

ladoA = int(input('Digite o tamanho de um dos lados do triângulo:'))
ladoB = int(input('Digite o tamanho de um outro lado do triângulo:'))
ladoC = int(input('Digite o tamanho do último lado do triângulo:'))

if (ladoA + ladoB > ladoC) or (ladoA > ladoC > ladoB) or (ladoB + ladoC > ladoA):
    if ladoA == ladoB == ladoC:
        print('Este é um triângulo equilátero')
    elif (ladoA == ladoB) or (ladoA == ladoB) or (ladoB == ladoC):
        print('Este é um triângulo isóceles')
    else:
        print('Este é um triângulo escaleno')
else:
    print('Não é possível formar um triângulo com essas proporções.')