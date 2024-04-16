'''
FUNÇÕES LAMBDA, OU FUNÇÃO ANÔNIMA, SÃO UM FORMATO DE FUNÇÃO PARA SER APLICADO APENAS UMA VEZ E DE FORMA RESUMIDA, PODENDO SER ESCRITA EM ATÉ MESMO APENAS UMA LINHA, E QUE NÃO PRECISA SER DEFINIDA. SUA SINTAXE É A SEGUINTE:
'''
#lambda variável: expressão

'''
COMO EXEMPLO, VAMOS CRIAR UMA FUNÇÃO PADRÃO E UMA FUNÇÃO LAMBDA QUE FAÇAM A MESMA COISA: RECEBER UM VALOR E MULTIPLICAR ESSE VALOR POR 2:
'''
#numero = int(input('Digite um número para ser multiplicado por 2:'))

#FUNÇÃO PADRÃO
def dobraNumero(num):
    dobro = num * 2
    return dobro

#print(dobraNumero(numero))

#FUNÇÃO LAMBDA
dobro = lambda num: num * 2

#print(dobro(numero))

'''
PERCEBA QUE O RESULTADO É O MESMO EM AMBAS AS VERSÕES, PORÉM É MAIS SUSCINTO NA VERSÃO LAMBDA/ANÔNIMA.

É FREQUENTEMENTE TAMBÉM USADO JUNTO DA FUNÇÃO MAP(), QUE IRÁ EXECUTAR AQUELA FUNÇÃO EM CADA ITERÁVEL DE UMA LISTA, POR EXEMPLO
'''
listaNotas = [10.0, 8.5, 9.25, 6.5, 7.0, 5.0, 6.5]

notasDuplicadas = map(lambda num: num * 2, listaNotas)
notasDuplicadas = list(notasDuplicadas)
#print(notasDuplicadas)

'''
FOI NECESSÁRIO UTILIZAR TAMBÉM O LIST, ALÉM DO MAP, PORQUE QUANDO UTILIZAMOS O MAP NO PRIMEIRO 'notasDuplicadas', CRIAMOS UM OBJETO DO TIPO MAP. PARA QUE ESSE VALOR ENTÃO SEJA EXIBIDO, É NECESSÁRIO QUE SEJA CONVERTIDO EM UMA LISTA COM O MÉTODO LIST()
'''
