'''
PARA FAZER A DECLARAÇÃO DE UMA FUNÇÃO EM PYTHON, FUNCIONA DA SEGUINTE FORMA:
'''
# def nomeDaFuncao(argumentos):
#     código da função

def mediaNotas(notaUm, notaDois, notaTres):
    soma = notaUm + notaDois + notaTres
    media = round(soma / 3, 2)
    return media #Só é possível atribuir o resultado de uma função em uma variável quando o 'return' é utilizado

primeiraNota = float(input('Digite a primeira nota do aluno:'))
segundaNota = float(input('Digite a segunda nota do aluno:'))
terceiraNota = float(input('Digite a terceira nota do aluno:'))

valorMedia = mediaNotas(primeiraNota, segundaNota, terceiraNota) 
print(valorMedia)

'''
TYPE HINT, DEFAULT VALUE, E DOCSTRING

SÃO TRÊS FORMAS DE DEIXAR O CÓDIGO MAIS LEGÍVEL E ACESSÍVEL, CADA UMA IMPLEMENTANDO UMA FUNCIONALIDADE DIFERENTE. O DOCSTRING, POR EXEMPLO, SÃO JUSTAMENTE ESSES COMENTÁRIOS, QUE NORMALMENTE SÃO USADOS PARA EXPLICAR UMA FUNÇÃO, MÉTODO, TRECHO DE UM CÓDIGO...
JÁ O TYPE HINT IRÁ DAR UMA DICA A RESPEITO DA FUNÇÃO, INFORMANDO O TIPO DE SEUS ARGUMENTOS E RETORNO, AO PASSAR O MOUSE POR CIMA DA FUNÇÃO. A SINTAXE É A SEGUINTE:
'''
# def nomeDaFuncao(argumento: tipoArgumento) -> tipoRetorno:
# código da função

'''
JÁ O DEFALT VALUE, COMO O NOME SUGERE, É UM VALOR QUE É DADO AOS ARGUMENTOS DE UMA FUNÇÃO, CASO NENHUM OUTRO SEJA PASSADO. ACRESCENTANDO O DEFAULT VALUE NO CÓDIGO ACIMA, TEMOS:
'''
# def nomeDaFuncao(argumento: tipoArgumento = defaultValue) -> tipoRetorno:
# código da função
'''
TRAZENDO DE EXEMPLO A FUNÇÃO ACIMA, MAS IMPLEMENTANDO ESSAS MELHORIAS:
'''
def mediaNotasComDica(notaUm: float = 0, notaDois: float = 0, notaTres: float = 0) -> float:
    '''
    notaUm: valor da primeira nota
    notaDois: valor da segunda nota
    notaTrês: valor da terceira nota
    '''
    soma = notaUm + notaDois + notaTres
    media = round(soma / 3, 2)
    '''
    É feita a soma dos valores das três notas e, posteriormente, tirada a média do resultado. O resultado dessa média será o retorno da função
    '''
    return media

valorMediaDois = mediaNotasComDica(primeiraNota, segundaNota, terceiraNota)
print(valorMediaDois)

'''
CLARO QUE NESTE CASO SIMPLES, IMPLEMENTAR ESSAS FUNCIONALIDADES NÃO SÃO TÃO NECESSÁRIAS, JÁ QUE O CÓDIGO NORMALMENTE É LEGÍVEL E DE FÁCIL COMPREENSÃO, COMO O PRIMEIRO EXEMPLO DA FUNÇÃO MAIS ACIMA. MAS NO CASO DE UMA IMPLEMENTAÇÃO QUE TENHA MUITAS LINHAS DE CÓDIGO E DIVERSAS FUNCIONALIDES, É INDISPENSÁVEL O USO DE UMA BOA DOCUMENTAÇÃO
'''