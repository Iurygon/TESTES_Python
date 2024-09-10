from modelos.cardapio.itenscardapio import ItemCardapio
#PROCESSO FEITO PARA IMPORTAR UM MÓDULO PARA OUTRO

class Bebida(ItemCardapio): #INDICA QUE UMA CLASSE HERDA CARACTERÍSTICAS DE OUTRA
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)   #CHAMA MÉTODOS DA CLASSE MÃE, NESSE CASO, O CONSTRUTOS
        self.tamanho = tamanho

    def __str__(self):
        return self._nome
    
    def aplicarDesconto(self):              #CONFORME EXPLICADO NA CLASSE DE ItemCardapio, O MÉTODO 'aplicarDesconto', POR SER ABSTRATO, É OBRIGATÓRIO NAS CLASSES FILHAS E DEVE SER 
        self._preco -= self._preco * 0.08   #IMPLEMENTADO CONFORME A NECESSIDADE NAS MESMAS