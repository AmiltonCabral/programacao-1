# (c) amiltoncristian9@gmail.com
# Creation Date: 13-05-2021
# Last Modified: Thu 13 May 2021 10:04:24 -03
# 

def gera_triangular_inferior(M):
    if len(M) < 2: return M
    xN = 0
    for y in range(len(M)):
        for x in range(xN):
            M[y][x] = M[y][x] + M[x][y]
            M[x][y] = 0
        M[y][xN] = M[y][xN]
        xN += 1

    return M


# M[1][0] = M[1][0] + M[0][1]
# M[2][0] = M[2][0] + M[0][2]
# M[2][1] = M[2][1] + M[1][2]

M = [[1, 2, 3, 4],
     [5, 6, 2, 4],
     [2, 7, 8, 1],
     [4, 5, 6, 7]]
gera_triangular_inferior(M)
assert M == [[1, 0, 0, 0],
             [7, 6, 0, 0],
             [5, 9, 8, 0],
             [8, 9, 7, 7]]
N = [[1]]
assert gera_triangular_inferior(N) == [[1]]
O = [[]]
assert gera_triangular_inferior(O) == [[]] 
P = [[1, 2], [3, 4]]
assert gera_triangular_inferior(P) == [[1, 0], [5, 4]]
Q = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
assert gera_triangular_inferior(Q) == [[1, 0, 0],
                                       [6, 5, 0],
                                       [10,14,9]]
