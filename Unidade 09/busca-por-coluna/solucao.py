# (c) amiltoncristian9@gmail.com
# Creation Date: 03-05-2021
# Last Modified: seg 03 mai 2021 08:21:30
# Busca todos os indices na qual determinado número está em uma matriz

def busca_todos_por_coluna_em_matriz(m, e):
    lista_indices = []
    if len(m) > 0:
        for x in range(len(m[0])):
            for y in range(len(m)):
                if m[y][x] == e:
                    lista_indices.append((y, x))
    return lista_indices


'''matriz = [
    [2, 3, 5, 3, 1],
    [3, 2, 1, 5, 6],
    [3, 2, 3, 2, 1],]
print(busca_todos_por_coluna_em_matriz(matriz, 4))'''
