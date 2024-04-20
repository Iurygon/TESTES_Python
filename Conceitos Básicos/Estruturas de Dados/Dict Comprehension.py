'''
ASSIM COMO A LIST COMPREHENSION, O DICT COMPREHENSION É UMA FORMA MAIS CONCISA DE FAZER A CONSTRUÇÃO DE UM DICIONÁRIO. O FORMATO PADRÃO DO DICT COMPREHENSION É O SEGUINTE:
{chave: valor for item in lista}

COMO EXEMPLO, VAMOS CRIAR UM DICIONÁRIO COM BASE NA SEGUINTE LISTA DE LISTAS, CRIADA TAMBÉM USANDO LIST COMPREHENSION:
'''
listaCompleta = [[('João', 'J720'), ('Maria', 'M205'), ('José', 'J371'), ('Cláudia', 'C546'), ('Ana', 'A347')],
                  [[8.0, 9.0, 10.0], [9.0, 7.0, 6.0], [3.4, 7.0, 7.0], [5.5, 6.6, 8.0], [6.0, 10.0, 9.5]],
                  [9.0, 7.3, 5.8, 6.7, 8.5],
                  ['Aprovado', 'Aprovado', 'Reprovado', 'Aprovado', 'Aprovado']]

colunas = ['Notas', 'Média Final', 'Situação']
cadastro = {colunas[i]: listaCompleta[i + 1] for i in range(len(colunas))}
'''
OU SEJA, A LISTA 'colunas' SERÁ ITERADA E CADA UM DE SEUS VALORES SERÁ UMA CHAVE. OS VALORES, POR SUA VEZ, SERÃO AS LISTAS PRESENTES EM 'listaCompleta', E, NOTA QUE O VALOR ESTÁ COMO
'i + 1', JÁ QUE O VALOR A PARTIR DE ONDE COMEÇARÁ SÃO AS NOTAS, E NÃO OS NOMES.

PARA FAZER A ADIÇÃO DOS NOMES, FICA DA SEGUINTE FORMA:
'''
cadastro['Estudante'] = [listaCompleta[0][i][0] for i in range(len(listaCompleta[0]))]

'''

AQUI, NESSE CASO, O DICIONÁRIO JÁ FOI CRIADO, POR ISSO A SINTAXE PARA INSERIR O VALOR SERÁ O PADRÃO PARA INSERIR VALOR EM UM DICIONÁRIO E, COMO O ELEMENTO A SER INSERIDO É UMA LISTA,
SERÁ FEITO USO DA LIST COMPREHENSION E NÃO DICT COMPREHENSION, AFINAL NÃO SERÁ INSERIDO UM DICIONÁRIO DENTRO DE OUTRO.
O QUE SERÁ ITERADO É O PRIMEIRO ELEMENTO DA 'listaCompleta', POR ISSO 'range(len(listaCompleta[0]))' A LISTA COM OS REGISTROS DOS ALUNOS.
E COMO O QUE QUEREMOS ESTA DENTRO DE UMA TUPLA, DENTRO DE UMA LISTA, DENTRO DE OUTRA LISTA, PRECISAMOS FAZER O USO DO 'listaCompleta[0][i][0]'
'''

print(cadastro)