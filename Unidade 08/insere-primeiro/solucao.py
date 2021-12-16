# (c) amiltoncristian9@gmail.com
# Creation Date: 28-04-2021
# Last Modified: qua 28 abr 2021 19:27:46
# Ordenar o primeiro número de uma lista

def insere_ordenado_primeiro(lista):
    for i in range(len(lista) -1):
        if lista[i] < lista[i+1]: break
        lista[i], lista[i+1] = lista[i+1], lista[i]


'''l1 = [5,2,6,9,11,13]
l2 = [7, 3, 6,6]
insere_ordenado_primeiro(l2)
print(l2)'''
