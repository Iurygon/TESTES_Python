'''
SETS, OU CONJUNTOS, SÃO UMA ESTRUTURA DE DADOS EM PYTHON QUE TEM COMO CARACTERÍSTICA NÃO SER ORDENADA E NÃO PERMITE REPETIÇÕES. FUNCIONA COMO UMA LISTA, PORÉM COM ESSAS CARACTERÍSTICAS.
'''
carros = {'Jetta Variant', 'Passat', 'Crossfox', 'Passat', 'Crossfox', 'Jetta Variant', 'Dodge Jorney'}
#print(carros)

'''
RODANDO O COMANDO ACIMA, NÓS PODEMOS PERCEBER QUE TANTO SÓ FORAM EXIBIDOS OS RESULTADOS ÚNICOS QUANTO A ORDEM DE EXIBIÇÃO DIFERE DÁ QUE FOI DECLARADA. POR ISSO, NÃO É POSSÍVEL ACESSAR UM ÚNICA ELEMENTO COMO EM UMA LISTA, POR EXEMPLO, DA SEGUINTE FORMA:

print(carros[0])

AFINAL, NÃO HÁ ELEMENTO DEFINIDO EM NENHUMA POSIÇÃO DO SET.

TAMBÉM É POSSÍVEL QUE UMA LISTA SEJA TRANSFORMADA EM UM CONJUNTO, DA SEGUINTE MANEIRA:
'''
novosCarros = ['Uninho', 'Gol Bolinha', 'Parati', 'Jetta Variant', 'Passat', 'Crossfox', 'Passat', 'Crossfox', 'Jetta Variant', 'Dodge Jorney']
#print(novosCarros, len(novosCarros))

conjuntoNovosCarros = set(novosCarros)
#print(conjuntoNovosCarros, len(conjuntoNovosCarros))

'''
PERCEBA QUE AS CARACTERÍSTICAS DO CONJUNTO PASSAM A SE APLICAR NA LISTA QUANDO CONVERTAMOS A MESMA PRA UM CONJUNTO.
'''

'''
OPERAÇÕES COM SETS

A TEORIA DOS CONJUNTOS TAMBÉM É APLICADA EM PYTHON, SENDO POSSÍVEL FAZER OPERAÇÕES DE DISJUNÇÃO, INTERSEÇÃO E UNIÃO COM OS CONJUNTOS CRIADOS
'''
acessorios_passat = {'Rodas de Liga', 'Travas Elétricas', 'Piloto Automático', 'Central Multimídia'}
acessorios_crossfox = {'Piloto Automático', 'Teto Panorâmico', '4 X 4', 'Central Multimídia'}
acessorios_jetta = {'Controle de Estabilidade', 'Câmbio Automático', 'Travas Elétricas', 'Rodas de Liga'}

'''
PARA VERIFICAR A DISJUNÇÃO, OU SEJA, SE NÃO HÁ ELEMENTOS EM COMUM ENTRE OS CONJUNTOS, PODEMOS O USAR O MÉTODO DO OBJETO SET '.isdisjoint()', QUE IRÁ RETORNAR VERDADEIRA OU FALSO SE HOUVER ELEMENTOS EM COMUM OU NÃO, RESPECTIVAMENTE:
'''
#print(set.isdisjoint(acessorios_passat, acessorios_crossfox))
#print(set.isdisjoint(acessorios_crossfox, acessorios_jetta))

'''
PARA VERIFICAR INTERSEÇÃO ENTRE OS CONJUNTOS, PODEMOS USAR TANTO O MÉTODO '.intersection' QUANTO O COMANDO '&' (AND), E O RESULTADO SERÁ UM CONJUNTO COM OS ELEMENTOS SEMELHANTES. CASO NÃO HOUVER NENHUM, O RESULTADO SERÁ UM CONJUNTO VAZIO:
'''
#print(set.intersection(acessorios_passat, acessorios_crossfox))
#print(acessorios_jetta & acessorios_crossfox)
#print(acessorios_jetta & acessorios_crossfox & acessorios_passat)

'''
POR FIM, PARA A UNIÃO, PODEMOS FAZER ATRAVÉS DO MÉTODO '.union' OU DO COMANDO '|' (OR), TENDO COMO RESULTADO UM CONJUNTO DA UNIÃO DOS CONJUNTOS PASSADOS:
'''
print(set.union(acessorios_crossfox, acessorios_passat, acessorios_jetta))
print(acessorios_jetta | acessorios_crossfox | acessorios_passat | {'Assento ejetor'})


'''
PARA FINALIZAR, UMA GRANDE VANTAEM DO SET É A SUA PERFORMANCE, VISTO QUE ELE EXECUTA MAIS RÁPIDO QUE UMA LISTA OU TUPLA, POR EXEMPLO, O QUE PODE SER UMA GRANDE VANTAGEM NA HORA DE TRABALHAR COM MUITOS DADOS.
'''