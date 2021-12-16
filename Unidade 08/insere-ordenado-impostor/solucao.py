# (c) amiltoncristian9@gmail.com
# Creation Date: 24-04-2021
# Last Modified: sáb 24 abr 2021 15:34:32
# Identificar o impostor de uma lista e o colocar em sua posição correta

def insere_ordenado_impostor(lista):
    tamanho_lista = len(lista)
    impostor, lista_aux = [], []
    impostor_entrou = False
    for i in range(1, len(lista)):
        if lista[i] < lista[i-1]:
            impostor.append(lista.pop(i))
            break
    while len(lista) > 0:
        lista_aux.append(lista.pop(0))
    for i in range(len(lista_aux)):
        if i == tamanho_lista: break
        if not impostor_entrou and impostor[0] < lista_aux[i]:
            lista.append(impostor[0])
            impostor_entrou = True
        lista.append(lista_aux[i])
    if not impostor_entrou:
        lista.append(impostor[0])


'''l = [10, 5, 20, 40]
ll = [1, 2, 4, 3, 5, 6, 7, 11]
ll = [1, 9, 11, 3, 14]
insere_ordenado_impostor(l)
print(l)'''
