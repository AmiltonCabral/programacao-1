# (c) amiltoncristian9@gmail.com
# Creation Date: 24-04-2021
# Last Modified: sáb 24 abr 2021 19:54:30
# Retornar o indice de uma lista na qual o valor é igual a um número N

def ultimo_indice(num, lista):
    saida = -1
    for i, numero_lista in enumerate(lista):
        if num == numero_lista:
            saida = i
    return saida


'''print(ultimo_indice(2, [15,2,13,11,14,2]))
print(ultimo_indice(42, [15,2,13,11,14,2]))'''
