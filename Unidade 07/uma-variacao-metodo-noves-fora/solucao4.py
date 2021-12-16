def noves_fora(numeros):
    lista = []

    if len(numeros) == 1:
        novo = numeros[0]
        if novo >= 9:
            lista.append(numeros[:])
            novo -= 9
            numeros.append(novo)
            numeros.pop(0)

    while len(numeros) > 1:
        lista.append(numeros[:])
        novo = (numeros[0] + numeros[1])
        if novo >= 9:
            novo -= 9
        numeros.append(novo)
        numeros.pop(0)
        if len(lista) > 0:
            numeros.pop(0)
        if len(numeros) > 1:
            for i in range(len(numeros)):
                for a in range(len(numeros) - 1, i, -1):
                    if numeros[a] > numeros[i]:
                        numeros[a], numeros[i] = numeros[i], numeros[a]
    lista.append(numeros)

    if lista[-1][0] == 9:
        novo = 0
        numeros.append(novo)
        numeros.pop(0)
    saida = (lista[-1][0], lista)
    return saida
