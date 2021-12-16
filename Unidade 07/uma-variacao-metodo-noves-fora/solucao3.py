def meu_slice(lista, ini, fim):
    nova_lista = []
    for i in range(ini, fim):
        nova_lista.append(lista[i])

    return nova_lista


def noves_fora(numeros_lista):
    lista_res = []
    lista_res.append(numeros_lista)
    entrou = False
    while len(numeros_lista) > 1:
        entrou = True
        soma = (numeros_lista[0] + numeros_lista[1]) % 9

        lista_aux = meu_slice(numeros_lista, 2, len(numeros_lista))

        numeros_lista = [soma]
        numeros_lista += lista_aux

        if len(numeros_lista) > 1:
            if numeros_lista[0] < numeros_lista[1]:
                numeros_lista[0], numeros_lista[1] = numeros_lista[1], numeros_lista[0]
        
        lista_res.append(numeros_lista)

    if not entrou:
        if numeros_lista[0] == 9:
            lista_res.append([numeros_lista[0] % 9])

        return (lista_res[-1][0], lista_res) 

    return (numeros_lista[0], lista_res)
