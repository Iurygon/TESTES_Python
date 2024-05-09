import pyautogui    as pa
'''
A BIBLIOTECA PYAUTOGUI É USADA PARA FAZER A AUTOMATIZAÇÃO DE PROCESSOS VIA PYTHON, PODENDO SIMULAR CLIQUES DO MOUSE E ATALHOS DE TECLADO, POR EXEMPLO, PARA TORNAR PROCESSOS MAIS ÁGEIS.
VEJAMOS ALGUNS EXEMPLOS DE USO DA BIBLIOTECA, FAZENDO A AUTOMATIZAÇÃO DO CADASTRO DES PRODUTOS EM UMA TABELA SQL
'''
import time
'''
A BIBLIOTECA TIME SERÁ USADA PARA SETAR UM INTERVALO DE TEMPO DURANTE O CÓDIGO COM O MÉTODO SLEEP. ISSO PORQUE, DURANTE O PROCESSAMENTO DO CÓDIGO, A EXECUÇÃO PODE SER MAIS RÁPIDA DO
QUE O PROCESSO DOS PROGRAMAS NO DISPOSITIVO, ENTÃO SERÁ NECESSÁRIO RETARDAR ALGUMAS PARTES PARA GARANTIR QUE O AMBIENTE ESTEJA PRONTO PARA CONTINUAR O PROCESSO
'''
import pandas       as pd
'''
A BIBLIOTECA PANDAS É USADA PARA ANÁLISE DE DADOS. NÃO SERÁ APROFUNDADA AQUI, MAS É UMA FERRAMENTA EXTREMAMENTE ÚTIL E SERÁ USADA AQUI PARA FAZER A ABERTURA DO ARQUIVO ONDE ESTÃO OS
DADOS, COM O COMANDO A SEGUIR:
'''
dadosProd = pd.read_csv('produtos.csv')

'''AGORA, FAREMOS A AUTOMATIZAÇÃO COM OS COMANDOS DO PYAUTOGUI'''

pa.click()