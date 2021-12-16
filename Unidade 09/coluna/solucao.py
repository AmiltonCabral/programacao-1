# (c) amiltoncristian9@gmail.com
# Creation Date: 03-05-2021
# Last Modified: seg 03 mai 2021 10:23:50
# Retorna a coluna indicada de uma matriz

def coluna(matriz, i):
    coluna_de_i = []
    for y in range(len(matriz)):
        coluna_de_i.append(matriz[y][i])
    return coluna_de_i


'''M = [[1,4,1,1],[2,3,2,2],[3,2,3,3]]
print(coluna(M,1))'''
