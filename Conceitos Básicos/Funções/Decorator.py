#UM DECORATOR NADA MAIS É QUE UMA FUNÇÃO QUE RECEBE OUTRA COMO ARGUMENTO, RETORNANDO ESSA FUNÇÃO 'INTERIOR' COM ALGUMAS MODIFICAÇÕES
def decorator(func):
    def wrapper():
        print(f'A função "{func.__name__}" está sendo decorada pela função decorator.')
        func()
        print('Fim do decorator')
    return wrapper

@decorator
def ola():
    print('Olá!')

#TENDO A FUNÇÃO E O DECORATOR CRIADO, PODEMOS EXECUTAR USANDO O @ + O NOME DO DECORATOR SOBRE A FUNÇÃO A SER CHAMADA, COMO FOI ACIMA. DEPOIS, BASTA CHAMAR A FUNÇÃO QUE FOI DECORADA
ola()