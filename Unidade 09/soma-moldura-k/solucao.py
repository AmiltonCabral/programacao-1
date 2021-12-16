# (c) amiltoncristian9@gmail.com
# Creation Date: 03-05-2021
# Last Modified: seg 03 mai 2021 14:47:26
# Soma elementos da moldura escolhida em uma matriz quadrada

def soma_moldura(m, k):
    k_simetrico = len(m) -1 -k
    soma = 0
    for y in range(len(m)):
        for x in range(len(m[y])):
            if y == k and k <= x <= k_simetrico:
                soma += m[y][x]
            elif y == k_simetrico and k <= x <= k_simetrico:
                soma += m[y][x]
            elif x == k and k <= y <= k_simetrico:
                soma += m[y][x]
            elif x == k_simetrico and k <= y <= k_simetrico:
                soma += m[y][x]
    return soma


'''M = [[1,  2,  3,  4 ],
     [5,  6,  7,  8 ],
     [9,  10, 11, 12],
     [14, 15, 16, 17]]
N = [[1,   2,  3,  4, 55],
     [5,   6,  7,  8, 66],
     [9,  10, 11, 12, 77],
     [14, 15, 16, 17, 88],
     [95, 96, 97, 98, 99]]
print(soma_moldura(M, 1))'''
