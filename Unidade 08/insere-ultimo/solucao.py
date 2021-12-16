# (c) amiltoncristian9@gmail.com
# Creation Date: 27-04-2021
# Last Modified: ter 27 abr 2021 14:45:40
# Coloca o ultimo item da lista dentro da lista de forma crescente

def insere_ordenado_ultimo(lista):
    ultimo_elemento = lista.pop()
    lista_aux = []
    tamanho_lista = len(lista)

    for i in range(tamanho_lista):
        lista_aux.append(lista.pop(0))
    
    entrou = False
    for i in lista_aux:
        if not entrou and ultimo_elemento <= i:
            lista.append(ultimo_elemento)
            entrou = True
        lista.append(i)
    if not entrou:
        lista.append(ultimo_elemento)


'''l1 = [4,5]
insere_ordenado_ultimo(l1)
print(l1)'''
