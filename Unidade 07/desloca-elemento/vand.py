def desloca(lista, origem, destino):
    armazenamento = lista
    lista = []
    for i in range(len(armazenamento)):
        if i == destino:
            lista.append(armazenamento[i])
            lista.append(armazenamento[origem])
        elif i != origem:
            lista.append(armazenamento[i])
#        print(lista)
        print(l1)
    return lista


l1 = [2,6,9,11,13,5]
desloca(l1, 2, 4)
print(l1)
#assert l1 == [2,6,11,13,9,5]

'''l1 = [0,1,2,3,4,5,6]
desloca(l1, 4, 6)
assert l1 == [0,1,2,3,5,6,4]'''
