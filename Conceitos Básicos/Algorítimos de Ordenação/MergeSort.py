#UTILIZA DA IDEIA DE DIVIDAR PARA CONQUISTAR. AQUI, UM ARRAY É RECURSIVAMENTE DIVIDIDO EM PARTES MENORES PARA QUE SEJA REFORMULADO DEPOIS DE FORMA ORDENADA
array = [2, 9, 1, 3, 50, 20, 31, 4, 8, 10, 13, 36, 45, 7]

def mergeSort(arrayDesordenado):
    #CASO O TAMANHO DO ARRAY SEJA UM, NÃO É NECESSÁRIO DIVIDIR NOVAMENTE
    if len(arrayDesordenado) <= 1:
        return arrayDesordenado
    
    pontoCentral = len(arrayDesordenado) // 2
    listaEsquerda = arrayDesordenado[:pontoCentral]
    listaDireita = arrayDesordenado[pontoCentral:]
    
    listaEsquerda   = mergeSort(listaEsquerda)
    listaDireita    = mergeSort(listaDireita)

    return juntaArray(listaEsquerda, listaDireita)

def juntaArray(listaEsquerda, listaDireita):
    #SE O TAMANHO DA LISTA FOR 0, NÃO TEM PORQUE SEGUIR COM A VERIFICAÇÃO
    if len(listaEsquerda) == 0:
        return listaDireita
    if len(listaDireita) == 0:
        return listaEsquerda
    
    #DEFINE O ARRAY DE RESULTADO E OS ÍNDICES QUE SERÃO UTILIZADOS NA VERIFICAÇÃO PARA ORDENAÇÃO
    resultado = []
    indexEsquerda = indexDireita = 0

    while len(resultado) < len(listaEsquerda) + len(listaDireita):
        #CASO O ITEM DA ESQUERDA FOR MENOR OU IGUAL AO DA DIREITA, ELE SERÁ ADICIONADO PRIMEIRO NA LISTA DE RESULTADO. SENÃO, ACONTECE O CONTRÁRIO
        if listaEsquerda[indexEsquerda] <= listaDireita[indexDireita]:
            resultado.append(listaEsquerda[indexEsquerda])
            indexEsquerda += 1
        else:
            resultado.append(listaDireita[indexDireita])
            indexDireita += 1

        if indexDireita == len(listaDireita):
            resultado.extend(listaEsquerda[indexEsquerda:])
            break
        if indexEsquerda == len(listaEsquerda):
            resultado.extend(listaDireita[indexDireita:])
            break

    return resultado
    
print(mergeSort(array))