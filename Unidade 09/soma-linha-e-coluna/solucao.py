# (c) amiltoncristian9@gmail.com
# Creation Date: 01-05-2021
# Last Modified: sáb 01 mai 2021 17:15:51
# Soma elementos em determinada linha e coluna de uma matriz exceto o da linha e coluna

def soma_linha_e_coluna(matriz, l_y, c_x):
    soma_elementos = 0
    for y in range(len(matriz)):
        for x in range(len(matriz[y])):
            if y == l_y and x != c_x:
                soma_elementos += matriz[y][x]
            if x == c_x and y != l_y:
                soma_elementos += matriz[y][x]
    return soma_elementos


'''matriz = [
    [2, 3, 5, 3, 1],
    [3, 2, 1, 5, 6],
    [3, 2, 3, 2, 1],]
print( soma_linha_e_coluna(matriz,0,0) )'''
