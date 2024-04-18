'''
CRIE UM CÓDIGO QUE RECEBA CINCO NOTAS, DE 0 A 10, ELIMINE A MAIOR E A MENOR NOTA, E DEPOIS APRESENTE A MÉDIA DAS TRÊS NOTAS RESTANTES:
'''
listaNotas = []
media = 0

for i in range(0, 5):
    nota = int(input('Digite aqui o valor da nota (0 a 10):'))
    listaNotas.append(nota)

'''

USANDO UM ALGORITMO DE ORDENAÇÃO:

for i in range(len(listaNotas)):
    minIndex = i
    for j in range(i + 1, len(listaNotas)):
        if listaNotas[j] < listaNotas[minIndex]:
            minIndex = j
    temp = listaNotas[i]
    listaNotas[i] = listaNotas[minIndex]
    listaNotas[minIndex] = temp

listaNotas.__delitem__(0)
listaNotas.__delitem__(-1)

'''


'''
USANDO MÉTODOS DE LISTA:

listaNotas.remove(max(listaNotas))
listaNotas.remove(min(listaNotas))

'''


media = sum(listaNotas) / 3
print(media)