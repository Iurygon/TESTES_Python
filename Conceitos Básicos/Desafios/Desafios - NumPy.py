#PUXAR E EFETUAR A LEITURA DOS DADOS DE UMA URL
import numpy as np

url = 'https://raw.githubusercontent.com/allanspadini/numpy/dados/citrus.csv'
dados = np.loadtxt(url, delimiter=',', usecols=np.arange(1,6,1), skiprows=1)


#SELECIONAR APENAS O PESO E DIÂMETRO DAS LARANJAS E TORANJAS E GERAR GRÁFICAS DA RELAÇÃO ENTRE PESO E DIÂMETRO
diamLaranja = dados[:5000, 0]
pesoLaranja = dados[:5000, 1]
diamToranja = dados[5000:, 0]
pesoToranja  = dados[5000:, 1]

import matplotlib.pyplot as plt

# plt.plot(pesoLaranja, diamLaranja)
# plt.show()

plt.plot(pesoToranja, pesoToranja)
plt.show()