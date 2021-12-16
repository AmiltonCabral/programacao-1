# (c) amiltoncristian9@gmail.com
# Creation Date: 01-05-2021
# Last Modified: sáb 01 mai 2021 17:30:04
# A partir dos menores elementos de duas matrizes cria uma nova

def matriz_menor(m1, m2):
    m3 = []
    for y in range(len(m1)):
        m3.append([])
        for x in range(len(m1[y])):
            if m1[y][x] <= m2[y][x]:
                m3[y].append(m1[y][x])
            else:
                m3[y].append(m2[y][x])
    return m3


'''M1 = [[1,2,3],
      [13,14,15],
      [7,8,9]]
M2 = [[10,11,12],
      [4,5,6],
      [7,8,9]]
M3 = [[1,2,3],
      [0,0,0],
      [7,8,9]]
print( matriz_menor(M1, M3) )'''
