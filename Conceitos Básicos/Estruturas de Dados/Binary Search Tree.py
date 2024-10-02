'''
SÃO ESTRUTURAS DE DADOS QUE ARMAZENAM OS DADOS TAL COMO OS GALHOS DE UMA ÁRVORES, SE DIVIDINDO EM PONTOS CHAMADADOS 'NODES', QUE POR SUA VEZ POSSUEM DOIS NODES FILHOS, APENAS (POR ISSO BINÁRIO). O NODE FILHO DA ESQUERDA
SERÁ SEMPRE MENOR QUE O NODE PAI, ENQUANTO QUE O NODE FILHO DA DIREITO SERÁ SEMPRE MAIOR.
UMA DAS FORMAS DE FAZER A IMPLEMENTAÇÃO É A SEGUINTE:
'''

class BinaryTree():
    def __init__(self, value) -> None:                  #INICIA UMA INSTÂNCIA DE BINARY TREE, COM UM ÚNICO VALOR E OS DEMAIS NODES DA ESQUERDA E DIREITA NULOS
        self.value = value
        self.right = None
        self.left  = None 
    
    def insert(self, value):                            #FUNÇÃO USADA PARA INSERIR VALORES. CASO ENCONTRE UM ESPAÇO VAZIO (NONE) PARA INSERIR O VALOR, NESSE NODE ENTÃO RECEBERÁ UMA NOVA INSTÂNCIA DA CLASSE
        if value < self.value:
            if self.left is None:
                self.left = BinaryTree(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BinaryTree(value)
            else:
                self.right.insert(value)

    def find(self, value):                              #REALIZA A BUSCA PELA BINARY TREE ATÉ ENCONTRAR O VALOR DESEJADO
        if value < self.value:
            if self.left is None:
                return 'Valor não encontrado'
            else:
                self.left.find(value)
        elif value > self.value:
            if self.right is None:
                return 'Valor não encontrado'
            else:
                self.right.find(value)
        else:
            return 'Valor encontrado'
        
'''
VALE RESSALTAR QUE, NORMALMENTE, CASO OS VALORES ESTEJAM BEM DISTRIBUÍDOS PELA BINARY TREE, ESTÁ É UMA ESTRUTURA DE DADOS QUE POSSUI DESEMPENHO MELHOR QUE UMA LISTA, POR EXEMPLO.
'''