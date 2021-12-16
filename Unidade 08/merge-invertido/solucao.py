# (c) amiltoncristian9@gmail.com
# Creation Date: 26-04-2021
# Last Modified: seg 26 abr 2021 11:12:12
# Criar uma lista decrescente a partir de duas listas crescentes

def merge_invertido(l1, l2):
    nova_lista, l1_aux, l2_aux = [], [], []
    for i in l1:
        l1_aux.append(i)
    for i in l2:
        l2_aux.append(i)
    while len(l1_aux) > 0 and len(l2_aux) > 0:
        if l1_aux[-1] > l2_aux[-1]:
            nova_lista.append(l1_aux.pop())
        elif l1_aux[-1] < l2_aux[-1]:
            nova_lista.append(l2_aux.pop())
        else:
            nova_lista.append(l1_aux.pop())
    while len(l1_aux) > 0 or len(l2_aux) > 0:
        if len(l1_aux) > 0:
            nova_lista.append(l1_aux.pop())
        if len(l2_aux) > 0:
            nova_lista.append(l2_aux.pop())
    return nova_lista
