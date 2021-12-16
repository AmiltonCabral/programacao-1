# (c) amiltoncristian9@gmail.com
# Creation Date: 27-04-2021
# Last Modified: ter 27 abr 2021 15:42:26
# Indicar o primeiro indice onde esta determinado número em uma lista

def busca(seq, valor):
    resultado = -1
    for i in range(len(seq)):
        if seq[i] == valor:
            resultado = i
            break
    return resultado

'''seq = [8, 9, 2, 3, 6, 10, 7, 9]
print(busca(seq, 1))'''
