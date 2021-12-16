# (c) amiltoncristian9@gmail.com
# Creation Date: 26-04-2021
# Last Modified: seg 26 abr 2021 15:37:12
# Organizar uma lista com apenas dois itens distintos de modo que todos os itens 1 fique no começo da lista

def separa_duas_cores(lista, cor1, cor2):
    local_cor1, local_cor2 = [], []
    for i in range(len(lista)):
        if lista[i] == cor1:
            local_cor1.append(i)
        else:
            local_cor2.append(i)

    for i in range(len(local_cor1)):
        lista[local_cor1[i]], lista[i] = lista[i], lista[local_cor1[i]]


'''l1 = ['a', 'a', 'b', 'a', 'b']
print( separa_duas_cores(l1, 'b', 'a') )
print(l1)'''
