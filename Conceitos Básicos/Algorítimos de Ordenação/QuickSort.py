#FUNCIONA SEMELHANTE AO MÉTODO MERGE SORT, PORÉM, NESSE DAQUI, É DEFINIDO UM ELEMENTO PIVÔ QUE SERÁ USADO DE REFERÊNCIA PARA DIVIDIR A LISTA EM SUBLISTAS COM ELEMENTOS QUE SÃO MENORES,
#MAIORES, E IGUAIS AO PIVÔ. NO FINAL, AS LISTAS SERÃO UNIDAS
array = [2, 9, 1, 3, 50, 20, 31, 4, 8, 10, 13, 36, 45, 7]

def quickSort(arrayDesordenado):
    if len(arrayDesordenado) < 2:
        return arrayDesordenado
    
    pivot = arrayDesordenado[len(arrayDesordenado) // 2]
    menores = []
    maiores = []
    iguais = []

    for item in arrayDesordenado:
        print(item)
        if item < pivot:
            menores.append(item)
        elif item == pivot:
            iguais.append(item)
        else:
            maiores.append(item)
            
    return  quickSort(menores) + iguais + quickSort(maiores)

print(quickSort(array))