from modelos.cardapio.itenscardapio import ItemCardapio

class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)
        self._descricao = descricao

    def __str__(self):
        return self._nome
    
    def aplicarDesconto(self):                  
        self._preco -= self._preco * 0.05       #CONFORME EXPLICADO NA CLASSE DE ItemCardapio, O MÉTODO 'aplicarDesconto', POR SER ABSTRATO, É OBRIGATÓRIO NAS CLASSES FILHAS E DEVE SER 
                                                #IMPLEMENTADO CONFORME A NECESSIDADE NAS MESMAS