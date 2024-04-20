'''
LIST COMPREHENSION É UMA MANEIRA CONCISA DE CRIAR LISTAS ONDE CADA ITEM SEJA RESULTADO DE UMA OPERAÇÃO APLICADA EM UM ELEMENTO DE OUTRO ITERÁVEL, POR EXEMPLO, OU CRIAR UMA SUBQUÊNCIA
DE ELEMENTOS QUE SATISFAÇAM UMA CERTA CONDIÇÃO
'''
'''DE EXEMPLO, VAMOS CRIAR UMA LISTA DE QUADRADOS:'''
# quadrados = []
# for x in range(10):
#     quadrados.append(x**2)

# print(quadrados)

'''PODEMOS FAZER O MESMO PROCESSO UTILANDO UMA FUNÇÃO ANÔNIMA'''
# quadrados = list(map(lambda x: x**2, range(10)))

# print(quadrados)

'''E UTILIZANDO LIST COMPREHENSION, QUE FICA MAIS LEGÍVEL E CONCISO'''
# quadrados = [x**2 for x in range(10)]

# print(quadrados)

'''
BASICAMENTE, UMA LIST COMPREHENSION CONSISTE EM UM PAR DE COLCHETES CONTENDO UMA EXPRESSÃO SEGUIDA DE CLÁUSULA FOR, SEGUIDA DE 0 OU MAIS CLÁUSULAS IF/FOR. O RESULTADO É UMA NOVA LISTA
RESULTANTE DAS AVALIAÇÕES PASSADAS NA EXPRESSÃO:

[expressão for item in lista]
'''

'''EXEMPLO: CRIAR UMA LISTA COM OS ELEMENTOS DE DUAS OUTRAS LISTAS SE OS ELEMENTOS FOREM DIFERENTES:'''

# combinacao = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]

# print(combinacao)
'''QUE É A MESMA COISA DE:'''
# combinacao = []

# for x in [1, 2, 3]:
#     for y in [3, 1, 4]:
#         if x != y:
#             combinacao.append((x, y))

# print(combinacao)

'''
DESAFIO:

CRIAR UMA LISTA DA SITUAÇÃO DOS ESTUDANTES EM QUE CASO A MÉDIA SEJA MAIOR OU IGUAL A 6, RECEBERÁ O VALOR 'APROVADO', E CASO CONTRÁRIO, RECEBERÁ 'REPROVADO'.
GERAR TAMBÉM UMA LISTA:
    . LISTA DE TUPLA COM O NOME DOS ESTUDANTES E SEUS CÓDIGOS.
    . LISTA DE LISTAS COM AS NOTAS DE CADA ESTUDANTE.
    . LISTA COM AS MÉDIAS DE CADA ESTUDANTE.
    . LISTA COM A SITUAÇÃO DOS ESTUDANTES DE ACORDO COM A MÉDIA.

NESTE CASO, COMO PRECISAREMOS USAR UMA ESTRUTURA CONDICIONAL COM IF E ELSE, A LISTA COMPREHENSION FICA DESSA FORMA:

[res_if if condicao else res_else for elemento in lista]
'''

nomes = [('João', 'J720'), ('Maria', 'M205'), ('José', 'J371'), ('Cláudia', 'C546'), ('Ana', 'A347')]
notas = [[8.0, 9.0, 10.0], [9.0, 7.0, 6.0], [3.4, 7.0, 7.0], [5.5, 6.6, 8.0], [6.0, 10.0, 9.5]]
medias = [9.0, 7.3, 5.8, 6.7, 8.5]
situacao = ['Aprovado(a)' if media >= 6 else 'Reprovado(a)' for media in medias]

'''AGORA, PARA CRIAR UMA LISTA COM ESTAS OUTRAS LISTA/TUPLAS, PODEMOS FAZER DA SEGUINTE FORMA:'''

cadastro = [x for x in [nomes, notas, medias, situacao]]

print(cadastro)