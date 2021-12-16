# (c) amiltoncristian9@gmail.com
# Creation Date: 30-04-2021
# Last Modified: sex 30 abr 2021 17:35:11
# Mostrar as diagonais de uma matriz

def diagonais(m):
    lista_diagonal = [[],[]]
    sequencia = 0
    for i in range(len(m)):
        lista_diagonal[0].append(m[i][i])
    for i in range(len(m) -1, -1, -1):
        lista_diagonal[1].append(m[sequencia][i])
        sequencia += 1

    return lista_diagonal


'''M = [[1,2,3],
     [4,5,6],
     [7,8,9]]
M = [[1, 2], [3, 4]
print(diagonais(M))'''
