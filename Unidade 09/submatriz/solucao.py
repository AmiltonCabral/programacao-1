# (c) amiltoncristian9@gmail.com
# Creation Date: 06-05-2021
# Last Modified: Mon 17 May 2021 15:25:44 -03
# Retorna uma matriz dentro de outra matriz

def verifica_existencia(A, p, q, r, s, m, n):
    indiceValido = (0 <= p <= m) and (0 <= r <= m) and (0 <= q <= n) and (0 <= s <= n)
    ehSubmatriz = (p <= r) and (q <= s)
    return indiceValido and ehSubmatriz


def nova_matriz(A, p, q, r, s):
    matriz = []
    for y in range(p, r + 1):
        linha = []
        for x in range(q, s + 1):
            linha.append(A[y][x])
        matriz.append(linha)
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
    saida = submatriz(M, 0, 0, 0, 1)
    for linha in saida:
        print(linha)


if __name__ == "__main__":
    testes()
