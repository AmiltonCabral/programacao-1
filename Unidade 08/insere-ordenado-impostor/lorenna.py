def remove_impostor(lista, impostor):
    for i in range(len(lista)):
        if lista[i] == impostor:
            lista.pop(i)
            return lista

def acha_impostor(lista):
    impostor = None
    for i in range(1, len(lista)):
        if lista[i] < lista[i - 1]:
            impostor = lista[i]
            return impostor

def insere_ordenado_impostor(lista):
    impostor = acha_impostor(lista)
    remove_impostor(lista, impostor)
    lista.append(impostor)
    for i in range(len(lista) - 1, -1, -1):
        if lista[i] > lista[i - 1]: break
        lista[i], lista[i - 1] = lista[i - 1], lista[i]

    return lista

lista = [10, 5, 20, 40]
print(insere_ordenado_impostor(lista))
