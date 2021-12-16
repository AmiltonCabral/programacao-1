# (c) amiltoncristian9@gmail.com
# Creation Date: 20-05-2021
# Last Modified: Thu 20 May 2021 13:13:08 -03
# Rotaciona lista 90 graus

def rotaciona90(imagem):
    imagem_rotacionada = []
    for lin in range(len(imagem[0])):
        imagem_rotacionada.append([])
        for col in range(len(imagem) -1, -1, -1):
            imagem_rotacionada[lin].append(imagem[col][lin])
            
    return imagem_rotacionada


I = [[1, 2, 3, 4, 5],
     [2, 3, 4, 5, 6],
     [3, 4, 5, 6, 7],
     [4, 5, 6, 7, 8]]
R = rotaciona90(I)
assert R == [[4, 3, 2, 1],
             [5, 4, 3, 2],
             [6, 5, 4, 3],
             [7, 6, 5, 4],
             [8, 7, 6, 5]]

J = [[1], [2]]
print(rotaciona90(J))
