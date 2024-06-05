import pandas as pd

'''
O PANDAS POSSUI ALGUNS MÉTODOS PARA QUE A IMPORTAÇÃO DOS DADOS SEJA FEITA, SENDO UM DELES O 'read_csv'. POR PADRÃO, O SEPARADOR DOS DADOS DE UM CSV É UMA VÍRGULA, PORÉM, É IMPORTANTE
VERIFICAR ANTES, JÁ QUE PODE SER QUE ESTEJA COM UM OUTRO SEPARADOR. NO CASO, O COMANDO 'sep', COMO A SEGUIR, É USADO PARA DEFINIR QUAL É O SEPARADOR USADO CASO NÃO SEJA A VÍRGULA.
NO EXEMPLO, É O PONTO E VÍRGULA
'''
url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'
dados = pd.read_csv(url, sep=';')
#print(url)

'''
PODEMOS VISUALIZAR QUANTOS LINHAS E COLUNAS DE DADOS POSSUÍMOS COM O MÉTODO 'shape':
'''
#print(dados.shape) #SAÍDA: 32960 LINHAS, 9 COLUNAS
'''
CASO QUEIRA VISUALIZAR SOMENTE ALGUNS DOS PRIMEIROS OU ÚLTIMOS DADOS, PODEMOS USAR OS SEGUINTE COMANDOS:
'''
# print(dados.head(10))
# print(dados.tail(7))
'''
TANTO O HEAD QUANTO O TAIL, POR PADRÃO, EXIBEM APENAS 5 LINHAS DE DADOS, MAS É POSSÍVEL PASSAR QUANTAS SERÃO AS LINHAS EXIBIDAS NOS ARGUMENTOS
'''
'''
JÁ PARA VISUALIZAR APENAS ALGUMAS DAS COLUNAS DO DATAFRAME, PODEMOS ACESSAR ESSA COLUNA USANDO COLCHETES:
'''
# print(dados['Tipo']) #APENAS UMA COLUNA
# print(dados[['Tipo', 'Bairro', 'Area']]) #MAIS DE UMA COLUNA

'''
PARA EXIBIR INFORMAÇÕES DO DATAFRAME, TEMOS O COMANDO 'info' E O 'dtypes'. COM DTYPES, VEMOS QUAIS OS TIPOS DE DADOS DE CADA COLUNA, JÁ COM O INFO, CONSEGUIMOS VER UM POUCO MAIS DE INFORMAÇÕES
'''
# print(dados.info())
# print(dados.dtypes)


'''
ANÁLISE EXPLORATÓRIA

SE TRATA DE UMA ANÁLISE EM QUE BUSCAMOS ENTENDER COMO OS DADOS ESTÃO ESTRUTURADOS E COMPREENDER CERTAS CARACTERÍSTICAS COMO: VALARES PRESENTES, TIPOS DE ESTRUTURA DE DADOS, SE ELES SÃO QUALITATIVOS OU QUANTITATIVOS,
SE HÁ VALORES FALTANTES OU INCOMUNS. SENDO ASSIM, QUALQUER PERGUNTA SOBRE OS DADOS SÃO BEM-VINDAS E, DE EXEMPLO, IREMOS TOMAR AS DUAS PERGUNTAS A SEGUIR COMO BASE:

1. QUAIS OS VALORES MÉDIOS DE ALUGUEL POR TIPO DE IMÓVEL
2. QUAL O PERCENTUAL POR CADA TIPO DE IMÓVEL NA BASE DE DADOS
'''

'''
1. QUAIS OS VALORES MÉDIOS DE ALUGUEL POR TIPO DE IMÓVEL

ANALISANDO A PERGUNTA, VEMOS QUE OS DADOS QUE MAIS IMPORTAM PARA ESSA QUESTÃO SÃO OS DADOS DA COLUNA 'VALORES' E 'TIPO'. SENDO ASSIM, CONSEGUIMOS FAZER UMA CONSULTA NO DATAFRAME, AGRUPANDO OS DADOS POR TIPO E TIRANDO
A MÉDIA DELES COM OS COMANDOS 'groupby' E 'mean'
'''
# print(dados.groupby('Tipo').mean(numeric_only=True)) #NUMERIC ONLY É USADA PARA GARANTIR QUE APENAS OS VALORES NUMÉRICOS SEJAM AGREGADOS PELA FUNÇÃO MEAN
'''
PODEMOS TAMBÉM VISUALIZAR APENAS A COLUNA DE VALORES, QUE MAIS INTERESSA, E AINDA ORDENAR OS DADOS:
'''
#print(dados.groupby('Tipo')[['Valor']].mean().sort_values('Valor'))
'''
COM ESSA ANÁLISE DOS DADOS, É POSSÍVEL VERIFICAR QUE AS MÉDIAS DE IMÓVEIS COMERCIAIS SÃO BEM MAIORES QUE AS DE IMÓVEIS RESIDENCIAIS, O QUE PODE PREJUDICAR PARA ANÁLISES FUTURAS. SENDO ASSIM, SERÃO FILTRADOS OS VALORES
DOS IMÓVEIS COMERCIAIS PARA QUE APENAS OS RESIDENCIAIS SEJAM EXIBIDOS E TENHAMOS MAIS CLAREZA EM SEUS DADOS.
PARA ISSO, PRECISAMOS DESCOBRIR QUAIS SÃO OS TIPOS IMÓVEIS PRESENTES:
'''
# print(dados.Tipo.unique()) #TAMBÉM É POSSÍVEL ACESSAR UMA COLUNA DA TABELA COM UM PONTO, COMO FOI FEITO AQUI
'''
OS VALORES DE IMÓVEIS COMERCIAIS SERÃO IDENTIFICADOS E ARMAZENADOS EM UMA VARIÁVEL:
'''
imoveisCom = [  'Conjunto Comercial/Sala', 
                'Prédio Inteiro', 'Loja/Salão', 
                'Galpão/Depósito/Armazém', 
                'Casa Comercial', 'Terreno Padrão',
                'Loja Shopping/ Ct Comercial',
                'Box/Garagem', 'Chácara',
                'Loteamento/Condomínio', 'Sítio',
                'Pousada/Chalé', 'Hotel', 'Indústria']

'''
EM SEGUIDA, SERÁ FEITA UMA QUERY COM UTILIZANDO ESSES VALORES. UMA QUERY NADA MAIS É QUE UM MÉTODO DO PANDAS PARA FILTRAR LINHAS ESPECÍFICAS DE UM DATA FRAME COM BASE EM UMA CONDIÇÃO:
'''
dadosResidenciais = dados.query('@imoveisCom not in Tipo') #NA QUERY, AS VARIÁVEIS PRECISAM SEM REFERENCIADAS COM UM @
# print(dadosResidenciais)
'''
AGORA QUE OS DADOS DOS IMÓVEIS COMERCIAIS NÃO IRÃO MAIS IMPACTAR NA ANÁLISE, PODEMOS VERIFICAR NOVAMENTE:
'''
# print(dadosResidenciais.groupby('Tipo')[['Valor']].mean().sort_values('Valor'))
'''
É NOTÁVEL QUE, MESMO QUE AINDA HAJA UMA DIFERENÇA ENTRE OS VALORES, NÃO ESTÁ NADA TÃO IMPACTANTE QUANTO ANTES. ALÉM DISSO, FOI ENCONTRADA A RESPOSTA PARA A PRIMEIRA PERGUNTA:
'''

'''
2. QUAL O PERCENTUAL POR CADA TIPO DE IMÓVEL NA BASE DE DADOS

PARA FAZER A VERIFICAÇÃO DO PERCENTUAL DOS DADOS, FAREMOS UMA CONTAGEM DOS VALORES COM O MÉTODO VALUE_COUNTS:
'''
# print(dadosResidenciais.Tipo.value_counts())
'''
TENDO O TOTAL DE DADOS, BASTA ENTÃO ADICIONAR O ARGUMENTO 'normalize = True' NO VALUE_COUNTS PARA QUE SEJA CONVERTIDO EM PORCENTAGEM. ALÉM DISSO, SERÁ FEITA A ORDENAÇÃO DOS VALORES PELA COLUNA 'TIPO', MAS PARA ISSO
TAMBÉM SERÁ NECESSÁRIO USAR O MÉTODO 'to_frame', PARA CONVERTER A SERIES EM UM DATAFRAME ANTES, PARA QUE AÍ SIM FUNCIONA A ORDENAÇÃO
'''
# print(dadosResidenciais.Tipo.value_counts(normalize=True).to_frame().sort_values('Tipo'))


'''
TRATANDO VALORES NULOS

O TRATAMENTO DE VALORES NULOS EM UMA BASE DE DADOS É EXTREMAMENTE IMPORTANTE PARA QUAISQUER ATIVIDADES QUE ENVOLVAM TAIS DADOS. AFINAL, OS VALORES NULOS PODEM OCASIONAR EM PROBLEMAS COMO ERROS DE TIPOS DE DADOS, 
CAUSAR DIVERGÊNCIAS EM RELATÓRIOS, ETC. PARA FAZER A VERIFICAÇÃO DOS VALORES EM PYTHON, COM O PANDAS, PODEMOS USAR O MÉTODO 'isnull', QUE RETORNA UM BOOLEANO SE HÁ ALGUM RESULTADO É NULO OU NÃO:
'''
# print(dadosResidenciais.isnull())
'''
PARA UMA MELHOR EFICIÊNCIA EM ENCONTRAR SE HÁ TAIS VALORES, PODEMOS FAZER A SOMATÓRIA TOTAL DELES, AO INVÉS DE TER QUE ANÁLISAR O DATA FRAME COMPLETAMENTE
'''
# print(dadosResidenciais.isnull().sum()) SAÍDA:
#                                           Tipo             0
#                                           Bairro           0
#                                           Quartos          0
#                                           Vagas            0
#                                           Suites           0
#                                           Area             0
#                                           Valor            9
#                                           Condominio    1865
#                                           IPTU          6879
'''
ASSIM, FOI VERIFICADO QUE EXISTEM VALORES NULOS NAS COLUNAS 'Valor', 'Condominio' E 'IPTU'. SENDO ASSIM, SERÁ FEITO O TRATAMENTO DOS VALORES, SUBSTITUINDO ELES POR '0' COM A FUNÇÃO 'fillna.
'''
dadosResidenciais = dadosResidenciais.fillna(0)
# print(dadosResidenciais.isnull().sum()) SAÍDA:'
#                                         Tipo          0
#                                         Bairro        0
#                                         Quartos       0
#                                         Vagas         0
#                                         Suites        0
#                                         Area          0
#                                         Valor         0
#                                         Condominio    0
#                                         IPTU          0