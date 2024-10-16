#FAZ A VERIFICAÇÃO EM PARES DOS ELEMENTOS, TROCANDO ELES DE LUGAR CASO NÃO ESTEJAM ORDENADOS
array = [2, 9, 1, 3, 50, 20, 31, 4, 8, 10, 13, 36, 45, 7]
size = len(array)


print(array)

for i in range(size):
    ordenado = True
    for j in range(size - i - 1):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
            ordenado = False #SE NÃO HOUVER TROCAS, ENTÃO O ELEMENTO JÁ ESTÁ ORDENADO
    if ordenado:
        break

print(array)
    