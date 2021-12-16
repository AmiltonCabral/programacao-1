# (py) amiltoncristian9@gmail.com
# Creation Date: 19-04-2021
# Last Modified: seg 19 abr 2021 15:09:03
# Organizar uma lista de forma decrescente
# Para transformar em ordem crescente só inverter < por > na linha 15

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
        lista.pop(indice)
        nova_lista.append(maior)

    return nova_lista

print( lista_decrescente([444,23,6,3,2,0,6,8,5,3,2,4,5,3,5,5,3,345,345,345,5,23,0,13,4,4,5,550]) )
