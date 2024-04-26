'''
AS EXCEÇÕES SÃO ERROS QUE OCORREM DURANTE O FUNCIONAMENTO DO CÓDIGO, SEJA POR ENTRADA INCORRETA DA DADOS OU FALTA DE REFERÊNCIA INCORRETA A ALGUMA VARIÁVEL, POR EXEMPLO.
CONSEGUIMOS FAZER O TRATAMENTO DESSAS EXCEÇÕES USANDO OS MÉTODOS 'TRY' E 'EXCEPT', SENDO QUE O 'TRY' IRÁ TENTAR FAZER A EXECUÇÃO DO CÓDIGO QUE CONTÉM E, CASO OCORRA ALGUM ERRO, 
SERÁ ENCERRADA A SUA EXECUÇÃO E INICIARÁ A EXECUÇÃO DO 'EXCEPT', QUE TEM A FUNÇÃO DE APRESENTAR MAIS INFORMAÇÕES A RESPEITO DO ERRO QUE FOI ENCONTRADO.
A SINTAXE É A SEGUINTE:
'''
# try:
#   Código a ser executado. Em caso de erro, encerra imediatamente.
# except nomeDaExcecao as e:
#   Se uma exceção é lançada no try, esse código será rodado. Senão, irá pular essa etapa.

'''
EXEMPLO:
ERRO QUE OCORRE AO CHAMAR A CHAVE INCORRETA EM UM DICIONÁRIO:
'''
notas = {'João': [8.0, 9.0, 10.0], 'Maria': [9.0, 7.0, 6.0], 'José': [3.4, 7.0, 8.0], 'Cláudia': [5.5, 6.6, 8.0], 
         'Ana': [6.0, 10.0, 9.5], 'Joaquim': [5.5, 7.5, 9.0], 'Júlia': [6.0, 8.0, 7.0], 'Pedro': [3.0, 4.0, 6.0]}
nome = input('Digite o nome do aluno para verificar suas notas:')
#print(notas['Iury'])

'''
COMO FOI PASSADA UMA CHAVE QUE NÃO EXISTE NO DICIONÁRIO, CASO O CÓDIGO ACIMA FOR RODADO, SERÁ EXIBIDA UMA MENSAGEM DE ERRO QUE, POR MAIS QUE APRESENTE AS INFORMAÇÕES NECESSÁRIAS
SOBRE O ERRO, NÃO É MUITO AMIGÁVEL PARA O USUÁRIO. SENDO ASSIM, PODEMOS USAR O EXCEPT JUSTAMENTE PRA APRESENTAR DE UMA FORMA MAIS AGRADÁVEL, DA SEGUINTE FORMA:
'''
# try:
#     print(f'As notas do aluno {nome} são {notas[nome]}')
# except Exception as e:
#     print(type(e), f'Erro: {e}')

'''
AQUI, SERÁ APRESENTADO ENTÃO APENAS A CLASSE DO ERRO, QUE É 'KeyError', E QUAL FOI O ERRO, OU SEJA, O NOME DIGITADO QUE NÃO EXISTE NO DICIONÁRIO.
PODEMOS ATÉ FAZER MELHOR E APONTAR DIRETAMENTE PARA APENAS ESSE TIPO DE ERRO ESPECÍFICO, AO INVÉS DE APONTAR PARA A CLASSE-MÃE 'Exception', QUE ENGLOBA TODAS EXCEÇÕES, E ATÉ INFORMAR
UMA MENSAGEM DE ERRO AINDA MAIS CLARA:
'''
# try:
#     print(f'As notas do aluno {nome} são {notas[nome]}')
# except KeyError:
#     print(f'Estudante {nome} não está matriculado na turma.')

'''
TEMOS TAMBÉM O 'ELSE', QUE ASSIM COMO NO 'IF...ELSE', PEGA O CASO CONTRÁRIO. OU SEJA, CASO NÃO HOUVER EXCEÇÕES, SERÁ EXECUTADO O CÓDIGO. SUA SINTAXE É:
'''
# try:
#   Código a ser executado. Em caso de erro, encerra imediatamente.
# except nomeDaExcecao as e:
#   Se uma exceção é lançada no try, esse código será rodado. Senão, irá pular essa etapa.
# else:
#   Código que será executado caso nenhuma exceção seja lançada.

'''
SEGUINDO A MESMA LINHA DE RACIOCÍNIO DOS CÓDIGOS ACIMA, PODEMOS VERIFICAR SE, CASO NÃO HOUVER EXCEÇÃO E REALMENTE EXISTIR AQUELE ALUNO, SUA MÉDIA É O SUFICIENTE PARA APROVAÇÃO.
'''
# try:
#     print(f'As notas do aluno {nome} são {notas[nome]}')
# except KeyError:
#     print(f'Estudante {nome} não está matriculado na turma.')
# else:
#     media = sum(notas[nome]) / 3
#     if media >= 6:
#         print('Aluno aprovado.')
#     else:
#         print('Aluno reprovado')

'''
POR FIM, TEMOS O 'FINALLY', QUE É EXECUTADO INDEPENDENTE SE HOUVER EXCEÇÃO OU NÃO:
'''
try:
    print(f'As notas do aluno {nome} são {notas[nome]}')
except KeyError:
    print(f'Estudante {nome} não está matriculado na turma.')
else:
    media = sum(notas[nome]) / 3
    if media >= 6:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado')
finally:
    print('Análise de notas do aluno finalizado!')