#Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase digitada mas com todas as letras maiúsculas.

frase = input('Digite uma frase:')
print(frase.upper())

#Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase digitada mas com todas as letras minúsculas.

frase = input('Digite uma frase:')
print(frase.lower())

#Crie uma variável chamada “`frase`” e atribua a ela uma string de sua escolha. Em seguida, imprima a frase sem espaços em branco no início e no fim.

frase = '       A vida é bela       '
print(frase.strip())

#Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase sem espaços em branco no início e no fim e em letras minúsculas.

frase = '            a vida como ela é     '
print(frase.upper().strip())

#Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase com todas as vogais “`e`” trocadas pela letra “`f`”.

frase = input('Digite uma frase: ')
print(frase.replace('e', 'f'))
