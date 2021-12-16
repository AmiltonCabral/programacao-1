# (py) amiltoncristian9@gmail.com
# Creation Date: 20-04-2021
# Last Modified: ter 20 abr 2021 10:59:13
# Remove valores abaixo de N de uma lista

def remove_menores(N, lista):
    continua, eliminados = True, 0
    while continua == True:
        continua = False
        for i in range(len(lista)):
            if lista[i] < N:
                continua = True
                eliminados += 1
                lista.pop(i)
                break
    return eliminados
