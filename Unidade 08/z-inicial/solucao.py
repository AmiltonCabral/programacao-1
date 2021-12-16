# (c) amiltoncristian9@gmail.com
# Creation Date: 26-04-2021
# Last Modified: seg 26 abr 2021 11:23:12
# Retorna quantas palavras na lista começam com a letra 'z'

def z_inicial(lista):
    inicia_z = 0
    for palavra in lista:
        if palavra[0] == 'z' or palavra[0] == 'Z':
            inicia_z += 1
    return inicia_z


lista_palavras = input().split()
print(z_inicial(lista_palavras))
