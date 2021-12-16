# (c) amiltoncristian9@gmail.com
# Creation Date: 10-05-2021
# Last Modified: Mon 10 May 2021 18:43:12 -03
# Agrupa resumo dos números

def meu_in(caractere, dic):
    for item in dic:
        if caractere == item:
            return True
    return False


def agrupa_resumos_iguais(lista):
    dic_resumo = {}
    for numero in lista:
        resumo = 0
        for caractere in str(numero):
            resumo += int(caractere)

        if meu_in(resumo, dic_resumo):
            dic_resumo[resumo].append(numero)
        else:
            dic_resumo[resumo] = [numero]

    return dic_resumo


lista1 = [60, 343, 19, 1230, 51, 123]
lista2 = [2]
lista3 = [30, 30]
lista4 = []
#print(agrupa_resumos_iguais(lista4))
assert agrupa_resumos_iguais(lista1) == {6:[60, 1230, 51, 123], 10:[343,19]}
assert agrupa_resumos_iguais(lista2) == {2:[2]}
assert agrupa_resumos_iguais(lista3) == {3:[30, 30]}
assert agrupa_resumos_iguais(lista4) == {}
