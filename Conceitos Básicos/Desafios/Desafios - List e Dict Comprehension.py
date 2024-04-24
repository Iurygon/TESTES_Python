#IMPRIMIR A SOMA DOS ELEMENTOS CONTIDOS NA LISTA
'''
listaDeListas = [[4,6,5,9], [1,0,7,2], [3,4,1,8]]
somaValores = [sum(i) for i in listaDeListas]
print(somaValores)
'''

#GERA UMA LISTA COM O TERCEIRO ELEMENTO DE CADA TUPLA CONTIDA NA LISTA ABAIXO
'''
listaDeTuplas = [('Pedro', 1.74, 81), ('Júlia', 1.65, 67), ('Otávio', 1.81, 83)]
listaElementos = [tupla[2] for tupla in listaDeTuplas]
print(listaElementos)
'''

#CRIAR UMA LISTA DE TUPLAS EM QUE, EM CADA TUPLA, O PRIMEIRO ELEMENTO SEJA A POSIÇÃO DO NOME NA LISTA E O SEGUNDO SEJA O PRÓPRIO NOME
'''
listaNomes = ['Pedro', 'Júlia', 'Otávio', 'Eduardo']
listaTuplasNomes = [(i, listaNomes[i]) for i in range(len(listaNomes))]
print(listaTuplasNomes)
'''

#ARMAZENA SOMENTE O VALOR NÚMERIO DE CADA TUPLA, SE O PRIMEIRO ELEMENTO FOR 'APARTAMENTO'
'''
aluguel = [('Apartamento', 1700), ('Apartamento', 1400), ('Casa', 2150), ('Apartamento', 1900), ('Casa', 1100)]
listaNumeros = [(tupla[1]) if tupla[0] == 'Apartamento' else (tupla) for tupla in aluguel]
print(listaNumeros)
'''

#CRIE UM DICIONÁRIO EM QUE AS CHAVES ESTÃO EM 'MESES' E OS VALORES ESTÃO EM 'DESPESAS'
'''
meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
despesa = [860, 490, 1010, 780, 900, 630, 590, 770, 620, 560, 840, 360]
dictDespesasMes = {meses[i]: despesa[i] for i in range(len(despesa))}
print(dictDespesasMes)
'''

#CRIAR UMA LISTA COM APENAS OS DADOS DE 2022 E QUE OS VALORES SEJAM MAIOR OU IGUAL A 6000
'''
vendas = [('2023', 4093), ('2021', 4320), ('2021', 5959), ('2022', 8883), ('2023', 9859), ('2022', 5141), ('2022', 7688), ('2022', 9544), ('2023', 4794), ('2021', 7178),
          ('2022', 3030), ('2021', 7471), ('2022', 4226), ('2022', 8190), ('2021', 9680), ('2022', 5616)]

vendasFiltradas = [tupla for tupla in vendas if tupla[0] == '2022' and tupla[1] >= 6000]
print(vendasFiltradas)
'''

#CATEGORIZAR OS VALORES DE GLICEMIA DA LISTA ABAIXO EM UMA LISTA DE TUPLAS USANDO O SEGUINTE CRITÉRIO:
# Glicose igual ou inferior a 70: 'Hipoglicemia'
# Glicose entre 70 a 99: 'Normal'
# Glicose entre 100 e 125: 'Alterada'
# Glicose superior a 125: 'Diabetes'
'''
glicemia = [129, 82, 60, 97, 101, 65, 62, 167, 87, 53, 58, 92, 66, 120, 109, 62, 86, 96, 103, 88, 155, 52, 89, 73]
catGlicemia = [('Hipoglicemia', glicose) if glicose <= 70 else
               ('Normal', glicose) if 70 < glicose <= 99 else
               ('Alterada', glicose) if 100 < glicose <= 125 else
               ('Diabetes', glicose) for glicose in glicemia]
print(catGlicemia)
'''

#CRIAR UMA LISTA DE TUPLAS EM QUE CADA TUPLA TENHA ID, QUANTIDADE, PREÇO E VALOR TOTAL (QUANTIDADE * PREÇO), NA QUAL A PRIMEIRA TUPLA É O CABEÇALHO DA TABELA
'''
id = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
quantidade = [15, 12, 1, 15, 2, 11, 2, 12, 2, 4]
preco = [93.0, 102.0, 18.0, 41.0, 122.0, 14.0, 71.0, 48.0, 14.0, 144.0]

listaTuplas = [('id', 'quantidade', 'preco', 'total')]
listaTuplas += [(id[i], quantidade[i], preco[i], quantidade[i] * preco[i]) for i in range(len(id))]

print(listaTuplas)
'''

#CRIE UM DICIONÁRIO EM QUE AS CHAVES SEJAM OS ESTADOS E O VALOR SEJA A QUANTIDADE DE FILIAIS NAQUELE ESTADO
'''
filialEstado = ['SP', 'ES', 'MG', 'MG', 'SP', 'MG', 'ES', 'ES', 'ES', 'SP', 'SP', 'MG', 'ES', 'SP', 'RJ', 'MG', 'RJ', 'SP', 'MG', 'SP', 'ES', 'SP', 'MG']
estados = list(set(filialEstado)) #USADA PARA FILTRAR APENAS OS VALORES ÚNICOS DOS ESTADOS
listaDeLista = []

for estado in estados:
    lista = [uf for uf in filialEstado if uf == estado]
    listaDeLista.append(lista)

dictFiliais = {estados[i]: len(listaDeLista[i]) for i in range(len(estados))}
print(dictFiliais)
'''

#CRIE UM DICIONÁRIO COM A QUANTIDADE DE FUNCIONÁRIOS POR FILIAL/ESTADO, E UM OUTRO DICIONÁRIO COM A SOMA DE FUNCIONÁRIOS POR ESTADO
'''
funcionarios = [('SP', 16), ('ES', 8), ('MG', 9), ('MG', 6), ('SP', 10), ('MG', 4), ('ES',9), ('ES', 7), ('ES', 12), ('SP', 7), ('SP', 11), ('MG',8), ('ES',8), ('SP',9), ('RJ', 13),
                ('MG', 5), ('RJ', 9), ('SP', 12), ('MG', 10), ('SP', 7), ('ES', 14), ('SP', 10), ('MG', 12)]

estadosUnicos = list(set([tupla[0] for tupla in funcionarios]))
listaAgregacao = []

for estado in estadosUnicos:
    listaAux = [tupla[1] for tupla in funcionarios if tupla[0] == estado]
    listaAgregacao.append(listaAux)

dictFuncFilial = {estadosUnicos[i]: listaAgregacao[i] for i in range(len(estadosUnicos))}
dictSomaFunc = {estadosUnicos[i]: sum(listaAgregacao[i]) for i in range(len(estadosUnicos))}

print(dictFuncFilial)
print(dictSomaFunc)
'''