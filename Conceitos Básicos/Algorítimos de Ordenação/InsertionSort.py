#A VERIFICAÇÃO É FEITA COM OS ITENS ANTERIORES, BUSCANDO A POSIÇÃO DO ITEM CHAVE ENTRE ELES
array = [2, 9, 1, 3, 50, 20, 31, 4, 8, 10, 13, 36, 45, 7]
size = len(array)

print(array)

for i in range(1, size):
    itemChave = array[i] 
    j = i - 1
    while j >= 0 and array[j] > itemChave:
        array[j + 1] = array[j]
        j -= 1
    array[j + 1] = itemChave

print(array)