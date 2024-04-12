from math import sqrt

numeros = [2, 8, 15, 23, 91, 112, 256]

for num in numeros:
    raiz = sqrt(num)
    if raiz // 1 == raiz:
        print(f'O número {raiz}, raiz de {num} é inteiro')
    else:
        print(f'O número {raiz}, raiz de {num}, não é inteiro')
