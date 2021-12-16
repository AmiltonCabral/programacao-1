# (py) amiltoncristian9@gmail.com
# Creation Date: 15-04-2021
# Last Modified: sex 16 abr 2021 18:11:19
# Aplicar o nove fora em uma sequência de números

def noves_fora(numeros_lista):
    lista = numeros_lista[:]
    lista_resultado = []
    for i in range(len(numeros_lista) +1):
        lista_resultado.append(lista[:])
    # Condição de parada
        if len(lista) == 1 and lista[0] < 9: break
    # Soma
        if len(lista) > 1:
            soma = (lista.pop(0) + lista.pop(0))
        else:
            soma = lista.pop(0)
    # Subtração
        if len(lista) >= 1:
            if soma >= 9:
                lista = [soma - 9] + lista
            else:
                lista = [soma] + lista
        else:
            if soma < 9:
                lista = [soma]
            else:
                lista = [0]
    # Organizar do maior para menor.
        if len(lista) > 1 and lista[0] < lista[1]:
            num_salvo = lista[0]
            lista[0] = lista[1]
            lista[1] = num_salvo

    return lista_resultado[len(lista_resultado)-1][0], lista_resultado
# [9, 1] da erro
print(noves_fora([9, 1]))

