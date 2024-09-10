from modelos.restaurante        import Restaurante
from modelos.cardapio.bebida    import Bebida
from modelos.cardapio.prato     import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Gui', 10)
restaurante_praca.receber_avaliacao('Lais', 8)
restaurante_praca.receber_avaliacao('Emy', 2)

cocaCola = Bebida('Refrigerante', 4.5, '350ml')

restaurante_praca.adicionarAoCardapio(cocaCola)

restaurante_praca.exibirCardapio

def main():
    pass
    #Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()