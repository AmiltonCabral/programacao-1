def meu_slice(lista, ini, fim):
    nova_lista = []
    for i in range(ini, fim):
        nova_lista.append(lista[i])

    return nova_lista


def lista_decrescente(lista):
    tamanho = len(lista)
    nova_lista = []

    while len(nova_lista) < tamanho:
        maior = lista[0]
        indice = 0
        for i in range(len(lista)):
            if lista[i] > maior:
                maior = lista[i]
                indice = i
            else:
                maior = maior
        lista.pop(indice)
        nova_lista.append(maior)

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

        numeros_lista = lista_decrescente(numeros_lista)
        print(id(numeros_lista))

        lista_res.append(numeros_lista)

    if not entrou:
        if numeros_lista[0] == 9:
            lista_res.append([numeros_lista[0] % 9])

        return (lista_res[-1][0], lista_res) 

    return (numeros_lista[0], lista_res)

#print( noves_fora([8, 7, 6, 5, 4, 2]) )
#print( noves_fora([9, 9, 1]) )
print( noves_fora([9, 7, 5, 4, 3, 1]) )
