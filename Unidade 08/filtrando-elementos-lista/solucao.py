# (c) amiltoncristian9@gmail.com
# Creation Date: 26-04-2021
# Last Modified: seg 26 abr 2021 12:09:14
# Retornar os números cuja indice seja divisível por num

def filtra_lista(num, numeros):
    nova_lista = []
    for i, numero in enumerate(numeros):
        if i % num == 0:
            nova_lista.append(numero)
    return nova_lista


'''numeros1 = [2,3,5,7,11,13,17]
print(filtra_lista(4, numeros1))'''
