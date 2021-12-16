# (py) amiltoncristian9@gmail.com
# Creation Date: 20-04-2021
# Last Modified: sáb 24 abr 2021 11:35:13
# Mover um elemento na lista até um determinado índice a direita

def desloca(lista, origem, destino):
    contagem = destino - origem
    i = origem
    while contagem > 0:
        lista[i], lista[i +1] = lista[i +1], lista[i]
        i += 1
        contagem -= 1

    return lista


l1 = [2,6,9,11,13,5]
desloca(l1, 2, 4)
print(l1)

