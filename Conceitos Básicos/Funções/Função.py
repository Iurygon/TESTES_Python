'''
PARA FAZER A DECLARAÇÃO DE UMA FUNÇÃO EM PYTHON, FUNCIONA DA SEGUINTE FORMA:
'''
# def nomeDaFuncao(argumentos):
#     código da função

def mediaNotas(notaUm, notaDois, notaTres):
    soma = notaUm + notaDois + notaTres
    media = soma / 3
    print(f'{media:.2f}')

primeiraNota = float(input('Digite a primeira nota do aluno:'))
segundaNota = float(input('Digite a segunda nota do aluno:'))
terceiraNota = float(input('Digite a terceira nota do aluno:'))

mediaNotas(primeiraNota, segundaNota, terceiraNota)