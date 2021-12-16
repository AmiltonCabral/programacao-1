# (c) amiltoncristian9@gmail.com
# Creation Date: 30-04-2021
# Last Modified: sex 30 abr 2021 19:51:05
# Move o objeto uma posição a direita do labirinto

def move_direita(labirinto):
    fim_busca = False
    for y in range(len(labirinto)):
        for x in range(len(labirinto[y])):
            if labirinto[y][x] == '*':
                posicao_objeto = [y, x]
                fim_busca = True
                break
        if fim_busca: break
    if len(labirinto[posicao_objeto[0]]) > posicao_objeto[1] + 1 and labirinto[posicao_objeto[0]][posicao_objeto[1]+1] == ' ':
        labirinto[posicao_objeto[0]][posicao_objeto[1]+1] = '*'
        labirinto[posicao_objeto[0]][posicao_objeto[1]] = ' '
        posicao_objeto[1] = posicao_objeto[1] + 1

    return (posicao_objeto[0], posicao_objeto[1])


'''labirinto1 = [
  [' ', ' ', ' '],
  ['p', '*', ' ']
]
for i in labirinto1:
    print(i)
print(move_direita(labirinto1))
for i in labirinto1:
    print(i)'''
