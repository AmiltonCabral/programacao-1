# (c) amiltoncristian9@gmail.com
# Creation Date: 11-05-2021
# Last Modified: Tue 11 May 2021 14:48:21 -03
# Verifica se um roteiro de voo eh possivel

def meu_in(iata_atual, iata_proximo, voos):
    for possiveis_voos in voos[iata_atual]:
        if possiveis_voos == iata_proximo:
            return True
    return False


def converte_roteiro_iata(locais_roteiro, iata):
    lista_iata = []
    for locais in locais_roteiro:
        lista_iata.append(iata[locais])
    return lista_iata


def verifica_validade(iata_roteiro, voos):
    for i in range(0, len(iata_roteiro) -1):
        if not meu_in(iata_roteiro[i], iata_roteiro[i+1], voos):
            return False
    return True


def eh_roteiro(iata, voos, roteiro):
    locais_roteiro = roteiro.split('/')
    iata_roteiro = converte_roteiro_iata(locais_roteiro, iata)
    if verifica_validade(iata_roteiro, voos):
        return True
    return False


iata ={"Campina Grande": "CPV",
       "Recife": "REC",
       "Salvador": "SSA",
       "Brasilia": "BSB",
       "Sao Paulo": "GRU",
       "Rio de Janeiro": "GIG"}

voos ={"CPV": ["REC", "SSA"],
       "REC": ["CPV", "BSB", "GRU", "GIG"],
       "SSA": ["REC", "GRU", "GIG"],
       "BSB": ["CPV", "GIG", "GRU"],
       "GRU": ["GIG", "BSB"],
       "GIG": ["GRU", "REC"]}

assert eh_roteiro(iata, voos, "Campina Grande/Recife/Rio de Janeiro")
assert eh_roteiro(iata, voos, "Sao Paulo/Rio de Janeiro/Recife/Brasilia")
assert not eh_roteiro(iata, voos, "Recife/Rio de Janeiro/Salvador/Recife")
