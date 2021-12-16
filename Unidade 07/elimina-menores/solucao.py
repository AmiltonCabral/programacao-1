# (py) amiltoncristian9@gmail.com
# Creation Date: 16-04-2021
# Last Modified: sex 16 abr 2021 21:12:55
# Elimina da lista os números menores que o informado

def elimina_menores(num, lista):
    copy_lista = lista
    n_removidos = 0
    for i in range(len(lista) -1, -1, -1):
        if lista[i] < num:
            copy_lista.pop(i)
            n_removidos += 1
    return n_removidos
