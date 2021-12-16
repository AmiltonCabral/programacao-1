# (c) amiltoncristian9@gmail.com
# Creation Date: 01-05-2021
# Last Modified: sáb 01 mai 2021 16:47:51
# Mostrar uma matriz dentro de outra matriz a partir de coordenadas

def soma_matriz_interna(matriz, inicio, fim):
    soma_matriz = 0
    for y in range(len(matriz)):
        for x in range(len(matriz[y])):
            if inicio[0] <= y <= fim[0] and inicio[1] <= x <= fim[1]:
                soma_matriz += matriz[y][x]
    return soma_matriz


'''M2 = [ [1, 2, 3], 
       [4, 5, 6], 
       [7, 8, 9] ]
print( soma_matriz_interna(M2, (1,1),(2,2)) )
M1 = [[1,3,5,2,7,8,30,-5],
      [9,-8,20,3,0,5,-7,12],
      [0,1,-2,-3,-10,5,1,20],
      [0,0,3,4,5,6,7,8],
      [7,7,-7,-7,7,-7,1,15]]
print( soma_matriz_interna(M1, (0,0), (1,1)) )'''
