'''
DECLARAÇÃO DE CLASSES DE OBJETOS EM PYTHON
'''
# class Musica():
#     nome    = ''
#     artista = ''
#     duracao = int

#UMA MANEIRA AINDA MAIS EFETIVA DE FAZER A CRIAÇÃO DE UMA CLASSE DE OBJETO, DE FORMA QUE SEJA DEFINIDO QUE TODAS AS NOVAS INSTÂNCIAS DAQUELE OBJETO JÁ POSSUAM DETERMINADAS CARACTERÍSTICAS, É USANDO O MÉTODO PRÓPRIO PRÓPRIO '__init__', DECLARADO COMO UA FUNÇÃO, E QUE JÁ INFORMA QUAIS SÃO, POR EXEMPLO, OS ATRIBUTOS QUE AQUELA CLASSE DE OBJETOS DEVE TER.

class Musica():
    listaDeMusicas  = []
    def __init__(self, nome, artista, duracao): #DECLARA UMA CONSTRUTOR DA CLASSE
        self._nome    = nome                    #AS UNDERLINES SÃO USADOS POR PADRÃO PARA INDICAR QUE UM ATRIBUTO DE UMA CLASSE NÃO DEVE SER ACESSADO DE OUTROS FORMAS QUE NÃO SEJAM
        self._artista = artista                 #POR MÉTODOS PRÓPRIOS. A ALTERAÇÃO É SIM POSSÍVEL, MAS POR CONVENSÃO, USANDO OS UNDERLINES, FICA CLARO PARA QUEM ESTÁ UTILIZANDO O CÓDIGO
        self._duracao = duracao                 #QUE ISSO NÃO DEVE SER FEITO
        Musica.listaDeMusicas.append(self)      
    def __str__(self):                          #MÉTODO QUE RETORNA EM STRING O QUE É INDICADO
        return f'Música {self._nome} do artista/banda {self._artista}'
    def listarMusicas():
        for musica in Musica.listaDeMusicas:
            print(f'Música: {musica._nome} | Artista/Banda: {musica._artista} | Duração: {musica._duracao} segundos')

    @property
    def _duracao():
        

#O PRIMEIRO PARÂMETRO PASSADO, 'self' INDICA QUE AQUELAS PROPRIEDADES SÃO PRÓPRIAS DAQUELE OBJETO, OU SEJA, CADA INSTÂNCIA DE UMA NOVA MÚSICA, NO EXEMPLO, TERÁ SEU PRÓPRIO NOME, ARTISTA E DURAÇÃO DEFINIDOS. EM SUMA, INDICA QUE AQUELA PROPRIEDADE EM QUESTÃO É DAQUELE OBJETO REFERENCIADO
#E UM DETALHE, O TERMO UTILIZADO FOI 'self', MAS PODERIA SER USADO QUALQUER OUTRO, CONTANDO QUE DEPOIS FOSSE FEITA A REFERÊNCIA 'termo.atributo'. O TERMO SELF É USADO NORMALMENTE POR CONVEÇÃO E PADRONIZAÇÃO

'''
CRIANDO NOVAS INSTÂNCIAS DESSA CLASSE
'''
# musica1 = Musica()
# musica1.nome    = 'Bohemian Rhapsody'
# musica1.artista = 'Queen'
# musica1.duracao = 244

# musica2 = Musica()
# musica2.nome    = 'Shape of You'
# musica2.artista = 'Ed Sheeran'
# musica2.duracao = 244

#DEFININDO UM CONSTRUTOR DO OBJETO, O __INIT__, FICA AINDA MAIS FÁCIL CRIAR UMA NOVA INSTÂNCIA DO MESMO

musica1 = Musica('Bohemian Rhapsody', 'Quenn', '355')
musica2 = Musica('Shape of You', 'Ed Sheeren', '244')

'''
VISUALIZANDO OS DADOS DE UM OBJETO
'''
# print(dir(musica1))     #EXIBE OS ATRIBUTOS, MÉTODOS E PROPRIEDADES DE UM OBJETO, TANTO NATIVOS QUANTO DECLARADOS PELO USUÁRIO
# print(vars(musica1))    #EQUIVALE AO MÉTODO __dict__, RETORNA UM DICIONÁRIO DESSES ATRIBUTOS E MÉTODOS 
print(musica1)
print(musica2)

Musica.listarMusicas()