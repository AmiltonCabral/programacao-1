# (c) amiltoncristian9@gmail.com
# Creation Date: 30-04-2021
# Last Modified: sex 30 abr 2021 17:59:39
# Retorna os indices de um determinado número em uma matriz

def busca_matriz(m, e):
    indices_elemento = []
    for y in range(len(m)):
        for x in range(len(m[y])):
            if m[y][x] == e:
                indices_elemento.append((y, x))
    return indices_elemento


'''matriz = [
    [2, 3, 5, 3, 1],
    [3, 2, 1, 5, 6],
    [1, 2, 3, 2, 1],
]
matriz = [[1, 2],[3, 4]]
print(busca_matriz(matriz, 5))'''
