# (c) amiltoncristian9@gmail.com
# Creation Date: 12-05-2021
# Last Modified: Wed 12 May 2021 08:28:11 -03
# Mostra o time campeão no campeonato

def descobrir_maior_ponto(dados):
    maior = 0
    for time in dados:
        if dados[time][0] > maior:
            maior = dados[time][0]
    return maior


def retornar_time_campeao(dados, pontuacao):
    resultado = []
    for time in dados:
        if dados[time][0] == pontuacao:
            resultado.append(time)
    return resultado


def time_campeao(dados):
    maior_ponto = descobrir_maior_ponto(dados)
    resultado = retornar_time_campeao(dados, maior_ponto)
    return resultado


dados ={"Botafogo": [59, 43, 39],
        "São Paulo": [52, 44, 36],
        "Palmeiras": [80, 62, 32],
        "Santos": [72, 59, 35]}
assert time_campeao(dados) == ["Palmeiras"]
