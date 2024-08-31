'''
DECLARAÇÃO DE CLASSES DE OBJETOS EM PYTHON
'''
class Musica():
    nome    = ''
    artista = ''
    duracao = int

'''
CRIANDO NOVAS INSTÂNCIAS DESSA CLASSE
'''
musica1 = Musica()
musica1.nome    = 'Bohemian Rhapsody'
musica1.artista = 'Queen'
musica1.duracao = 244

musica2 = Musica()
musica2.nome    = 'Shape of You'
musica2.artista = 'Ed Sheeran'
musica2.duracao = 244


'''
VISUALIZANDO OS DADOS DE UM OBJETO
'''
print(dir(musica1))     #EXIBE OS ATRIBUTOS, MÉTODOS E PROPRIEDADES DE UM OBJETO, TANTO NATIVOS QUANTO DECLARADOS PELO USUÁRIO
print(vars(musica1))    #EQUIVALE AO MÉTODO __dict__, RETORNA UM DICIONÁRIO DESSES ATRIBUTOS E MÉTODOS 
