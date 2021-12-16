# (c) amiltoncristian9@gmail.com
# Creation Date: 01-05-2021
# Last Modified: sáb 01 mai 2021 17:43:41
# A partir de uma matriz M, cria uma matriz T, onde T(ij) == M(ji)

def transposta(m):
    t = []
    for i in range(len(m[0])):
        t.append([])
    for y in range(len(m)):
        for x in range(len(m[y])):
            t[x].append(m[y][x])
    return t


'''M = [[1,1,1,1],
     [2,2,2,2],
     [3,3,3,3]]
print(transposta(M))'''
