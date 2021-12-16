# (c) amiltoncristian9@gmail.com
# Creation Date: 23-04-2021
# Last Modified: sex 23 abr 2021 17:09:21
# Criar um código a partir de um pseudocódigo

def bubblesort(dados):
    while True:
        swapped = False
        for i in range(len(dados) -1):
            if dados[i] > dados[i+1]:
                dados[i], dados[i+1] = dados[i+1], dados[i]
                swapped = True
        if not swapped: break

lista = [3,9,1,2]
bubblesort(lista)
print(lista)
