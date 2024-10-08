from abc import ABC, abstractmethod
#ABSTRACT BASE CLASSES É UMA BIBLIOTECA QUE PERMITE FAZER USO DE CLASSES E MÉTODOS ABSTRATOS EM PYTHON. CLASSES E MÉTODOS ABSTRATOS SÃO COMO UM 'ESQUELETO' PARA SUAS CLASSES FILHAS,
#ENTÃO NÃO SÃO COMPLETAMENTE DEFINIDOS PARA QUE A DEFINIÇÃO OCORRA NA PRÓPRIA CLASSE. NO EXEMPLO A SEGUIR, O MÉTODO ABSTRATO 'aplicarDesconto' ESTÁ SENDO DEFINIDO NA CLASSE 'ItemCardapio',
#ASSIM, TODAS AS CLASSES QUE HERDAREM DE ITEM CARDÁPIO DEVERÃO TER ESSE MÉTODO PRESENTE, DO CONTRÁRIO HAVERÁ UM ERRO NO CÓDIGO
class ItemCardapio(ABC):            #POR ABC SER UMA CLASSE, TEMOS QUE INDICAR QUE ItemCardapio HERDA SUAS CARACTERÍSTICAS
    def __init__(self, nome, preco):
        self._nome  = nome
        self._preco = preco

    @abstractmethod
    def aplicarDesconto(self):
        pass                    #O MÉTODO EM SI NÃO FAZ NADA, VISTO QUE SUA ÚNICA FUNÇÃO NESSE CLASSE É INDICAR A OBRIGATORIEDADE DESSE MÉTODO NAS CLASSES FILHAS, ONDE ELE SIM SERÁ
                                #IMPLEMENTADO DEVIDAMENTE E CONFORME A NECESSIDADE DE CADA CLASSE FILHA
