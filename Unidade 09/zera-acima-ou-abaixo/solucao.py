# (c) amiltoncristian9@gmail.com
# Creation Date: 30-04-2021
# Last Modified: sex 30 abr 2021 19:03:08
# Zerar alguns elementos em uma matriz de acordo com a especificação

def zerar_elementos(lista_coordenadas, matriz):
    for coordenada in lista_coordenadas:
        matriz[coordenada[0]][coordenada[1]] = 0


def zera_acima_ou_abaixo(m):
    soma_diagonal_baixo = 0
    soma_diagonal_acima = 0
    elementos_baixo_zerar = []
    elementos_acima_zerar = []
    for y in range(len(m)):
        for x in range(len(m[y])):
            if x == y: break
            else:
                soma_diagonal_baixo += m[y][x]
                elementos_baixo_zerar.append([y, x])
    for y in range(len(m)):
        liberado = False
        for x in range(len(m[y])):
            if x == y:
                liberado = True
                continue
            if liberado:
                soma_diagonal_acima += m[y][x]
                elementos_acima_zerar.append([y, x])
    if soma_diagonal_acima > soma_diagonal_baixo:
        zerar_elementos(elementos_acima_zerar, m)
    elif soma_diagonal_acima < soma_diagonal_baixo:
        zerar_elementos(elementos_baixo_zerar, m)
    else:
        zerar_elementos(elementos_acima_zerar, m)
        zerar_elementos(elementos_baixo_zerar, m)


'''M = [[1,2,3],
     [1,5,3],
     [1,6,9]]
zera_acima_ou_abaixo(M)
for i in M:
    print(i)'''
