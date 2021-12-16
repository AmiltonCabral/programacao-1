# (c) amiltoncristian9@gmail.com
# Creation Date: 06-05-2021
# Last Modified: Mon 17 May 2021 15:08:41 -03
# Retorna uma matriz dentro de outra matriz

def verifica_existencia(A, p, q, r, s, m, n):
    validacao = True
    if len(A) <= p:
        validacao = False
    elif len(A[p]) <= q:
        validacao = False
    elif len(A) <= r:
        validacao = False
    elif len(A[r]) <= s:
        validacao = False
    elif not p <= r <= m:
        validacao = False
    elif not q <= s <= n:
        validacao = False
    return validacao


def nova_matriz(A, p, q, r, s):
    matriz = []
    i = -1
    for y in range(len(A)):
        if p <= y <= r:
            matriz.append([])
            i += 1
        for x in range(len(A[y])):
            if p <= y <= r and q <= x <= s:
                matriz[i].append(A[y][x])
    return matriz


def submatriz(A, p, q, r, s):
    m = len(A)
    n = len(A[0])

    if not verifica_existencia(A, p, q, r, s, m, n):
        return None

    matriz_saida = nova_matriz(A, p, q, r, s)

    return matriz_saida


def testes():
    N = [[1,0,2,3,4,5,6]]
    M =[[11, 12, 13, 14, 15, 16],
        [21, 22, 23, 24, 25, 26],
        [31, 32, 33, 34, 35, 36],
        [41, 42, 43, 44, 45, 46],
        [51, 52, 53, 54, 55, 56],
        [61, 62, 63, 64, 65, 66],]
    O = [[1, 2],[3, 4]]
    P = [[1,2,3,4,5,6],[1,2,3,4,5],[1,2,3,4],[1,2,3],[1,2],[1]]
    Q = [[1,2,3,4],[5,6,7,8]]
    R = [[]]
    S = [[2], [3], [4], [5]]
    saida = submatriz(M, 1, 3, 3, 4)
    for linha in saida:
        print(linha)


if __name__ == "__main__":
    testes()

