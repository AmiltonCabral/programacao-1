# (c) amiltoncristian9@gmail.com
# Creation Date: 13-05-2021
# Last Modified: Thu 13 May 2021 09:17:21 -03
# Descobre quantas vagas tem a direita

def consulta_direita(labirinto):
    fim_busca = False
    for y in range(len(labirinto)):
        for x in range(len(labirinto[y])):
            if labirinto[y][x] == '*':
                posicao_objeto = [y, x]
                fim_busca = True
                break
        if fim_busca: break
    vagas_direita = 0
    if len(labirinto[0]) < 1 or len(labirinto) < 1: return vagas_direita
    while len(labirinto[posicao_objeto[0]]) > posicao_objeto[1] + 1:
        if not labirinto[posicao_objeto[0]][posicao_objeto[1]+1] == ' ': break
        vagas_direita += 1
        posicao_objeto[1] += 1
    return vagas_direita


labirinto1 = [
  ['P', '*', ' ', ' '],
  ['P', ' ', 'P', ' '],
  ['P', 'P', 'P', ' '] ]
assert consulta_direita(labirinto1) == 2
labirinto2 = [
  ['P', 'P', ' ', ' '],
  ['P', '*', 'P', ' '],
  ['P', 'P', 'P', ' '] ]
assert consulta_direita(labirinto2) == 0
labirinto3 = [[]]
assert consulta_direita(labirinto3) == 0
labirinto4 = [
  [' ', ' ', ' ', ' '],
  ['*', ' ', 'P', ' '] ]
assert consulta_direita(labirinto4) == 1
