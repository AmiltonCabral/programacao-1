# (c) amiltoncristian9@gmail.com
# Creation Date: 21-04-2021
# Last Modified: qua 21 abr 2021 14:49:52
# Organizar uma lista, inicio pares forma decrescente, fim ímpares forma crescente

def ajeita_lista(lista):
    i, contagem = 0, 0
    parada = len(lista) * len(lista)
    
    if len(lista) == 1:
        return None

    while contagem < parada:
        if lista[i] < lista[i+1]:
            lista[i], lista[i+1] = lista[i+1], lista[i]
        if i + 2 >= len(lista):
            i = 0
        else:
            i += 1
        contagem += 1

    for i in range(-1, -(len(lista) +1), -1):
        if lista[i] % 2 == 1:
            lista.append(lista.pop(i))


lista5 = [2]
lista2 = [9,8,7,6,5,4,3,2,1]
lista1 = [3, 2, 1, 4, 5, 6, 7, 8, 9]
lista3 = [8,4,7,2,9,5,1,3,6]
lista4 = [534,53,873,134,7,345,45,143,746,24,645,324,645,243,635,234,634,243,34,243,345,2347,6798,96,345,16,7,384,8,3805,944,3532,745]
print( ajeita_lista(lista5) )
print(lista5)
