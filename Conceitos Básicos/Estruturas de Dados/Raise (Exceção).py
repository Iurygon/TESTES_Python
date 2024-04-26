'''
UMA OUTRA FORMA DE USAR EXCEÇÕES É CRIANDO SUAS PRÓPRIAS EXCEÇÕES ATRAVÉS DO MÉTODO 'RAISE'. COM ELE, PODEMOS DEFINIR UM TIPO DE EXCEÇÃO QUE SERÁ CHAMADA QUANDO ALGO DETERMINADO OCORRER
NO CÓDIGO, E TRATAR NORMALMENTE COM OS TRATAMENTOS DE EXCEÇÕES. A SINTAXE DO RAISE É:
'''
# raise nomeDoErro ('Mensagem do erro')

'''
EXEMPLO:
CRIAR UMA FUNÇÃO QUE RECEBA UMA LISTA DE ATÉ TRÊS VALORES PARA TIRAR A MÉDIA, PORÉM, CASO A LISTA TENHA QUATRO OU MAIS VALORES, SERÁ INFORMADO UM ERRO
'''
def calculaMedia(lista: list = []) -> float:
    if len(lista) > 3:
        raise ValueError('A lista pode conter somente até três valores')
    media = sum(lista) / len(lista)
    return(media)

try:
    notas = [1, 3, '3']
    resultado = calculaMedia(notas)
except TypeError:
    print('Não foi possível calcular a média da nota, só são aceitos valores numéricos')
except ValueError as e:
    print(e)
except ZeroDivisionError:
    print('É necessário que tenha pelo menos um valor na lista')
else:
    print(f'O resultado é: {resultado:.2f}')
finally:
    print('Cálculo encerrado')