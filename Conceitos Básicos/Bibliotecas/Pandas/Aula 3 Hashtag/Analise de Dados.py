import pandas as pd

'''IMPORTAÇÃO DA TABELA'''
tabela = pd.read_csv('clientes.csv')
#print(tabela)

'''VERIFICANDO OS VALORES'''
# print(tabela.info())
# print(tabela.columns)

'''
VERIFICANDO, CONSEGUIMOS VER QUE NÃO HÁ VALORES NULOS NA TABELA, QUE DEVERIAM SER TRATADOS CASO HOUVESSE, PORÉM, VEJA QUE EXISTEM COLUNAS DO TIPO OBJECT. ISSO NA VERDADE SÃO TEXTOS, 
MAS OS MODELOS DE CLASSIFICAÇÃO NÃO CONSEGUEM TRABALHAR COM ELES.

PARA ISSO, VAMOS IMPORTAR A SEGUIR A BIBLIOTECA 'SKLEARN', PARA UTILIZAR O CODIFICADOR 'LABEL ENCODER'. COM ELE, CONSEGUIMOS TRANSFORMAR OS TEXTOS EM NÚMEROS PARA TRABALHARMOS COM
MODELOS DE CLASSIFICAÇÃO. DESSA FORMA, CADA INFORMAÇÃO DO TIPO TEXTO SERÁ CONVERTIDA EM UM NÚMERO, EX: PROFISSÃO -> CIENTISTA, PROFESSOR, MECÂNICO,... PROFISSÃO -> 0, 1, 2, ...
'''

from sklearn.preprocessing import LabelEncoder

codificador = LabelEncoder()

for coluna in tabela.columns:
    if tabela[coluna].dtype == 'object' and coluna != 'score_credito':
        tabela[coluna] = codificador.fit_transform(tabela[coluna])

for coluna in tabela.columns:
    if tabela[coluna].dtype == 'object' and coluna != 'score_credito':
        print(coluna)

# print(tabela)

'''
COM O CÓDIGO ACIMA, FIZEMOS ENTÃO A CONVERSÃO DOS DADOS PARA NÚMERO, COM EXCEÇÃO DA COLUNA 'SCORE_CREDITO', QUE SERÁ USADA.
'''

