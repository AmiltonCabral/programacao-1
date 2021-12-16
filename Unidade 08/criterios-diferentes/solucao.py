# (c) amiltoncristian9@gmail.com
# Creation Date: 26-04-2021
# Last Modified: ter 27 abr 2021 09:17:30
# Criar uma nova lista crescente a partir de outras duas listas

def ordena(lista1,lista2):
    nova_lista = []
    i_l1 = 0
    i_l2 = -1

    while i_l1 < len(lista1) and i_l2 +1 > -(len(lista2)):
        if lista1[i_l1] < lista2[i_l2]:
            nova_lista.append(lista1[i_l1])
            i_l1 += 1
        elif lista1[i_l1] > lista2[i_l2]:
            nova_lista.append(lista2[i_l2])
            i_l2 -= 1
        else:
            nova_lista.append(lista1[i_l1])
            i_l1 += 1

    while i_l1 < len(lista1):
        nova_lista.append(lista1[i_l1])
        i_l1 += 1
    while i_l2 +1 > -(len(lista2)):
        nova_lista.append(lista2[i_l2])
        i_l2 -= 1

    return nova_lista
