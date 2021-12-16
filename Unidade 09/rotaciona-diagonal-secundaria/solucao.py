# (c) amiltoncristian9@gmail.com
# Creation Date: 02-05-2021
# Last Modified: dom 02 mai 2021 20:58:03
# Rotacionar a diagonal secundaria de uma matriz para cima ou para baixo

def pegar_diagonal(matriz):
    i_x = -1
    diagonal = []
    for y in range(len(matriz)):
        diagonal.append(matriz[y][i_x])
        i_x -= 1
    return diagonal


def rotaciona_lista_diagonal(lista, direcao):
    if direcao == 'cima':
        primeiro_elemento = lista.pop(0)
        lista.append(primeiro_elemento)
        nova_lista = lista
    elif direcao == 'baixo':
        nova_lista = [lista.pop()]
        for i in lista:
            nova_lista.append(i)
    return nova_lista


def aloca_nova_diagonal(matriz, diagonal):
    i_x = -1
    for y in range(len(matriz)):
        matriz[y][i_x] = diagonal[y]
        i_x -= 1


def rotaciona_ds(matriz, direcao):
    diagonal = pegar_diagonal(matriz)
    diagonal = rotaciona_lista_diagonal(diagonal, direcao)
    aloca_nova_diagonal(matriz, diagonal)


'''M = [[1, 2, 3, 4 ], [5, 6, 7, 8 ], [9, 10, 11, 12], [14, 15, 16, 17]]
N = [[1, 2], [3, 4]]
rotaciona_ds(N, 'baixo')
print(N)'''
