import pandas as pd

tabela = pd.read_csv('cancelamentos.csv') #IMPORTA OS DADOS DO ARQUIVO DE CANCELAMENTOS
tabela = tabela.drop('CustomerID', axis=1) #REMOVE O TRECHO ESPECIFICADO DOS DADOS IMPORTADOS, NESSE CASO, A COLUNA CUSTOMER ID
#print(tabela)
tabela = tabela.dropna()
#print(tabela)

# print(tabela['cancelou'].value_counts())
# print(tabela['cancelou'].value_counts(normalize=True).map("{:.1%}".format))

'''
AQUI, COM O COMANDO 'value_counts', CONSEGUIMOS FAZER UMA CONTAGEM DOS VALORES, NESSE CASO, DO CAMPO 'cancelou'. DEPOIS, FOI USADO A MESMA FUNÇÃO PARA RETORNAR ESSES DADOS, MAS EM
PORCENTAGEM

AGORA, USANDO OS MESMOS COMANDOS, VAMOS ANALISAR A RELAÇÃO ENTRE OS CONTRATOS:
'''

# print(tabela['duracao_contrato'].value_counts)
# print(tabela['duracao_contrato'].value_counts(normalize=True))

'''
CONSEGUIMOS VER QUE O NÚMERO DE CONTRATOS MENSAIS É BEM INFERIOR COM RELAÇÃO AOS CONTRATOS ANUAIS E TRIMESTRAIS. SENDO ASSIM, VAMOS FAZER UMA ANÁLISE MAIS A FUNDO NOS MENSAIS PARA
VERIFICAR A RESPEITO:
'''

# print(tabela.groupby('duracao_contrato').mean(numeric_only=True))

'''
AQUI, O GROUP BY FOI USADO PARA AGRUPAR OS DADOS COM BASE NA COLUNA 'duracao_contrato' E DEPOIS FOI RETIRADA A MÉDIA COM A FUNÇÃO 'mean'. COM ISSO, FOI POSSÍVEL PERCEBER QUE, PARA OS
PLANOS MENSAIS, ESTÁ TENDO UM CANCELAMENTO DE 100% DOS CONTRATOS.

COM PARTE DOS PROBLEMAS JÁ IDENTIFICADO, OS DADOS DOS PLANOS MENSAIS SERÃO REMOVIDOS PARA CONTINUARMOS A ANÁLISE:
'''

tabela = tabela[tabela['duracao_contrato']!='Monthly'] #REMOVE OS VALORES 'Monthly' DA COLUNA 'duracao_contrato'
# print(tabela)
# print(tabela['cancelou'].value_counts())
# print(tabela['cancelou'].value_counts(normalize=True).map('{:.1%}'.format))

'''
AGORA FOI IDENTIFICADO QUE HÁ AINDA UMA PORCENTAGEM BEM ALTA DE CANCELAMENTOS, SENDO ASSIM, VAMOS OLHAR NOVAMENTE MAIS A FUNDO:
'''

# print(tabela['assinatura'].value_counts(normalize=True))
# print(tabela.groupby('assinatura').mean(numeric_only=True))

'''
NOVAMENTE UTILIZANDO DA CONTAGEM DE VALORES E DA MÉDIA DAS COLUNAS, MAS NÃO FOI DE MUITA SERVENTIA, TENDO EM VISTO QUE OS VALORES ESTÃO BEM SEMALHANTES. SENDO ASSIM, VAMOS CONTINUAR
BUSCANDO

COMO OS DADOS NÃO FORAM CONCLUSIVOS, VAMOS VERIFICAR ATRAVÉS DE GRÁFICOS PARA TERMOS UMA PERSPECTIVA MAIS CLARA DOS DADOS
'''

import plotly.express as px

for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color='cancelou', width=600)
    grafico.show()

'''
AQUI, IMPORTAMOS A BIBLIOTECA PLOTLY.EXPRESS PARA GERAR UM GRÁFICO REFERENTE A CADA COLUNA DA TABELA, OU SEJA, 11 GRÁFICOS.
'''