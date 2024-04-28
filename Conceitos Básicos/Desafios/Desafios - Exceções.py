#CRIAR UM CÓDIGO QUE RECEBA DOIS NÚMEROS E FAÇA A DIVISÃO ENTRE ELES, HAVENDO TRATAMENTO DE ERRO PARA DIVISÃO POR 0 E CASO UM DOS NÚMEROS SEJA UMA STRING
'''
num1 = float(input('Digite o dividendo:'))
num2 = float(input('Digite o divisor:'))

try:
    resultado = num1 / num2
    print(f'A divisão de {num1} por {num2} é {resultado}')
except ZeroDivisionError:
    print('O divisor não pode ser igual a zero')
except TypeError:
    print('O valor precisa ser um número, não uma string')
'''

#CRIE UM CÓDIGO QUE RECEBA 2 LISTAS COMO PARÂMETRO E RETORNA UMA LISTA DE TUPLAS COM TRÊS ELEMENTOS EM CADA TUPLA, SENDO O DOIS ELEMENTOS NA MESMA POSIÇÃO EM CADA LISTA E A SOMA DELES
#ALÉM DISSO, DEVE TER UM TRATAMENTO DE ERRO CASO AS LISTAS TENHAM TAMANHOS DIFERENTES E CASO UM DOS ELEMENTOS NÃO SEJA UM NÚMERO
'''
lista1 = [4,6,7,9,10]
lista2 = [-4,6,8,7, 'a']

try:
    if len(lista1) != len(lista2):
        raise IndexError ('As duas listas precisam ter o mesmo número de elementos')
    listaTuplas = [(lista1[i], lista2[i], lista1[i] + lista2[i]) for i in range(len(lista1))]
except IndexError as e:
    print(e)
except TypeError:
    print('As listas precisam ser apenas de números, sem conter strings')
else:
    print(listaTuplas)
finally:
    print('Código encerrado')
'''

#CRIE UM CÓDIGO QUE RECEBE UMA LISTA DE LISTAS COM AS NOTAS DE 3 ESTUDANTES EM UMA PROVA. CADA ESTUDANTE RESPONDEU 5 QUESTÕES E AS RESPOSTAS VARIAM DE 'A' ATÉ 'D'. CASO ALGUM VALOR
#QUE NÃO CONDIZ COM AS RESPOSTAS ACEITAS FOR INSERIDO, SERÁ NECESSÁRIO LANÇAR UM ERRO COM A MENSAGEM 'A alternativa [alternativa] não é uma opção de alternativa válida'