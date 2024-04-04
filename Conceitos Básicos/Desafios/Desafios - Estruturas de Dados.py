"""
Faça um programa que tenha a seguinte lista contendo os valores de gastos de uma empresa de papel `[2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]`. Com esses valores, faça um programa que calcule a média de gastos. Dica, use as funções built-in [`sum()`](https://docs.python.org/3/library/functions.html#sum) e [`len()`](https://docs.python.org/3/library/functions.html#len).
"""

valores = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]
media = sum(valores) / len(valores)

print('A média dos valores é ', media)

"""
 Com os mesmos dados da questão anterior, defina quantas compras foram acima de 3000 reais e calcule a porcentagem quanto ao total de compras.
"""

valores = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]
contador = 0

for val in valores:
    if val >= 3000:
        contador += 1

print(f'O total de valores acima de 3000 é {contador}, {(contador * 100) / len(valores)}% do total')

"""
Faça um programa que, ao inserir um número qualquer, criará uma lista contendo todos os números primos entre 1 e o número digitado.
"""

num = int(input('Digite um número:'))
listPrimo = []
contPrimo = 0

for i in range(1, num + 1):
    for j in range(1, num + 1):
        if i % j == 0:
            contPrimo += 1
    if contPrimo == 2:
        listPrimo.append(i)
    contPrimo = 0

print(listPrimo)

"""
Para um estudo envolvendo o nível de multiplicação de bactérias em uma colônia, foi coletado o número de bactérias multiplicadas por dia, com base em um processo de duplicação diária e pode ser observado a seguir: `[1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]`. Tendo esses valores, faça um código que gere uma lista contendo o percentual de crescimento de bactérias por dia, comparando o número de bactérias em cada dia com o número de bactérias do dia anterior. Dica: para calcular o percentual de crescimento usamos a seguinte equação: `100 * (amostra_atual - amostra_passada) / (amostra_passada)`.
"""

txCresc = [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]

for i in txCresc:
    if txCresc.index(i) == 0:
        print('Início da colônia com {} bactérias'.format(i))
        continue
    else:
        print('Houve uma taxa de crescimento de {:.2f}% e está em {}'.format(100 * (txCresc[txCresc.index(i)] - txCresc[txCresc.index(i) - 1]) / txCresc[txCresc.index(i) - 1], i))

"""
Uma empresa de e-commerce está interessada em analisar as vendas dos seus produtos. Os dados das vendas foram armazenados em um dicionário:
```
{'Produto A': 300, 'Produto B': 80, 'Produto C': 60,
 'Produto D': 200, 'Produto E': 250, 'Produto F': 30}
```
Escreva um código que calcule o total de vendas e o produto mais vendido.
"""

vendas = {'Produto A': 300, 'Produto B': 80, 'Produto C': 60,
          'Produto D': 200, 'Produto E': 250, 'Produto F': 30}
valorBase = 0

for chave, valor in vendas.items():
    if valor >= valorBase:
        valorBase = valor

print(f'O total de vendas foi {sum(vendas.values())} e o produto mais vendido foi {valorBase}.')

"""
Os funcionários de um setor da empresa que você trabalha vão receber um abono correspondente a 10% do seu salário devido ao ótimo desempenho do time. O setor financeiro solicitou sua ajuda para a verificação das consequências financeiras que esse abono irá gerar nos recursos. Assim, foi encaminhada para você uma lista com os salários que receberão o abono: `[1172, 1644, 2617, 5130, 5532, 6341, 6650, 7238, 7685, 7782, 7903]`. O abono de cada funcionário não pode ser inferior a 200. Em código, transforme cada um dos salários em chaves de um dicionário e o abono de cada salário no elemento. Depois, informe o total de gastos com o abono, quantos funcionários receberam o abono mínimo e qual o maior valor de abono fornecido.

"""
