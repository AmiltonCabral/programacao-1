# (c) amiltoncristian9@gmail.com
# Creation Date: 03-05-2021
# Last Modified: seg 03 mai 2021 08:06:03
# Retorna os índices do número encontrado na matriz

def busca_matriz(m, e):
    for y in range(len(m)):
        for x in range(len(m[y])):
            if m[y][x] == e:
                return (y, x)
