'''
CRIE UM CÓDIGO QUE RECEBE UMA FRASE DIGITADA PELO USUÁRIO E CRIE UMA LISTA CONSIDERANDO SOMENTE AS PALAVRAS COM 5 OU MAIS LETRAS
'''
frase = input('Digite aqui uma frase:')
listaPalavras = frase.split()
listaPalavrasMaiores = []

for palavra in listaPalavras:
    if len(palavra) >= 5:
        listaPalavrasMaiores.append(palavra)
    else:
        continue

print(listaPalavrasMaiores)