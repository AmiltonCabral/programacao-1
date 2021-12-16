# (c) amiltoncristian9@gmail.com
# Creation Date: 20-04-2021
# Last Modified: ter 20 abr 2021 19:33:19
# Adicionar um item a lista e manter em ordem alfabetica

def adiciona_item(item, lista):
    lista_aux = []
    for _ in range(len(lista)):
        lista_aux.append(lista.pop())

    continua = True
    while len(lista_aux) > 0 and len(item) > 0:
        if item < lista_aux[-1] and continua:
            lista.append(item)
            continua = False
        else:
            lista.append(lista_aux.pop())
            
    if continua:
        lista.append(item)
