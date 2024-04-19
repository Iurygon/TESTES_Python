'''
CRIE UMA FUNÇÃO QUE RECEBE DUAS LISTAS DE GOLS MARCADOS E SOFRIDOS POR UM TIME DE FUTEBOL, CALCULE A PONTUAÇÃO E O PERCENTUAL DE APROVEITAMENTO DO TIME. AS VITÓRIAS (GOLS MARCADOS > GOLS SOFRIDOS) VALEM 3 PONTOS, OS EMPATES (GOLS MARCADOS = GOLS SOFRIDOS), E AS DERROTAS (GOLS MARCADOS < GOLS SOFRIDOS) NÃO VALEM NADA.
'''
gols_marcados = [2, 1, 3, 1, 0]
gols_sofridos = [1, 2, 2, 1, 3]

def calcPontos(golsSof, golsMar):
    pontos = 0
    for partida in range(len(gols_marcados)):
        if golsMar[partida] > golsSof[partida]:
            pontos += 3
        elif golsMar[partida] == golsSof[partida]:
            pontos += 1
        else:
            continue
    aproveitamento = (pontos * 100 ) / (3 * len(gols_marcados))
    print(f'A pontuação do time ao final das partidas foi de {pontos}, um aproveitamento de {aproveitamento:.2f}%.')

calcPontos(gols_sofridos, gols_marcados)