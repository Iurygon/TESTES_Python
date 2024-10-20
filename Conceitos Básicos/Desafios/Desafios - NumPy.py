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

# plt.plot(pesoToranja, pesoToranja)
# plt.show()

#ENCONTRAR O COEFICIENTE ANGULAR E LINEAR PARA ENCONTRAR A RETA DA LARANJA E DA TORANJA
# xLaranja = pesoLaranja
# YLaranja = diamLaranja
# n = np.size(xLaranja)
# aLaranja = (n * np.sum(xLaranja * YLaranja) - np.sum(xLaranja) * np.sum(YLaranja)) / (n * np.sum(xLaranja**2) - np.sum(xLaranja)**2)
# bLaranja = np.mean(YLaranja) - aLaranja*np.mean(xLaranja)
# yLaranja = aLaranja * xLaranja + bLaranja

# xToranja = pesoToranja
# YToranja = diamToranja
# n = np.size(xToranja)
# aToranja = (n * np.sum(xToranja * YToranja) - np.sum(xToranja) * np.sum(YToranja)) / (n * np.sum(xToranja**2) - np.sum(xToranja)**2)
# bToranja = np.mean(YToranja) - aToranja*np.mean(xToranja)
# yToranja = aToranja * xToranja + bToranja

# plt.plot(xToranja, yToranja)
# plt.plot(pesoLaranja, diamLaranja)
# plt.plot(xLaranja, yLaranja)
# plt.plot(pesoLaranja, diamLaranja)
# plt.show()