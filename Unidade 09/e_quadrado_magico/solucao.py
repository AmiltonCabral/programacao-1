# (c) amiltoncristian9@gmail.com
# Creation Date: 03-05-2021
# Last Modified: seg 03 mai 2021 12:59:41
# Recebe matriz e retorna boolean se é quadrado mágico

def lista_igual(lista_somas):
    eh_igual = True
    for i in range(len(lista_somas)):
        if lista_somas[0] != lista_somas[i]:
            eh_igual = False
            break
    return eh_igual

 
def linha_magica(matriz):
    lista_somas = []
    for y in range(len(matriz)):
        soma_linha = 0
        for x in range(len(matriz[y])):
            soma_linha += matriz[y][x]
        lista_somas.append(soma_linha)
    return lista_somas


def coluna_magica(matriz):
    lista_somas = []
    if len(matriz) < 1: return []
    for x in range(len(matriz[0])):
        soma = 0
        for y in range(len(matriz)):
            soma += matriz[y][x]
        lista_somas.append(soma)
    return lista_somas


def diagonal_magica(matriz):
    if len(matriz) < 1 or len(matriz[0]) < 1: return []
    lista_somas, soma_dp, soma_ds = [], 0, 0
    x_dp = 0
    x_ds = -1
    for y in range(len(matriz)):
        soma_dp += matriz[y][x_dp]
        soma_ds += matriz[y][x_ds]
        x_dp += 1
        x_ds -= 1
    lista_somas.append(soma_dp)
    lista_somas.append(soma_ds)
    return lista_somas


def verifica_existe_repetido(matriz):
    lista_valores_matriz = []
    tem_repetido = False
    for y in matriz:
        for x in y:
            lista_valores_matriz.append(x)
    if len(lista_valores_matriz) < 2: return False
    for i in range(1, len(lista_valores_matriz)):
        if lista_valores_matriz[0] == lista_valores_matriz[i]:
            tem_repetido = True
    return tem_repetido


def eh_quadrado_magico(matriz):
    if matriz == [[]]:
        return True
    if len(matriz) > 0 and len(matriz) != len(matriz[0]):
        return False
    if verifica_existe_repetido(matriz):
        return False
    lista_somas = []
    lista_somas += linha_magica(matriz)
    lista_somas += coluna_magica(matriz)
    lista_somas += diagonal_magica(matriz)
    #print(lista_somas)
    return lista_igual(lista_somas)


'''quadrado1 = [[2,7,6],[9,5,1],[4,3,8]]
quadrado2 = [[2, 3], [3, 2]]
quadrado3 = [[0]]
quadrado3_2 = [[]]
quadrado4 = [[10,3,1,8],[5,4,2,11], [4,9,7,2], [3,6,12,1]]
quadrado5 = [[9, 8, 7, 6], [9, 8, 7, 6], [9, 8, 7, 6], [6,8,3,3]]
quadrado6 = [[2, 9, 4], [7, 5, 3], [6, 1, 8]]
quadrado7 = [[1,35,34,3,32,6],[30,8,28,27,11,7],[24,23,15,16,14,19],[13,17,21,22,20,18],
        [12,26,9,10,29,25],[31,2,4,33,5,36]]
quadrado8 = [[3, 2],[2, 3]]
print(eh_quadrado_magico(quadrado3))'''
