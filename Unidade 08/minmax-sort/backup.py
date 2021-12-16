# (c) amiltoncristian9@gmail.com
# Creation Date: 28-04-2021
# Last Modified: qua 28 abr 2021 21:39:31
# Criar o algoritimo de ordenação MinMax Sort

def copiar_lista(lista):
    nova_lista = []
    for i in lista:
        nova_lista.append(i)
    return nova_lista


def minmax_sort(lista):
    i_ini = 0
    i_fim = len(lista)
    resultado = []
    while True:
        menor = i_ini
        maior = i_fim-1
        for i in range(i_ini, i_fim):
            if lista[i] < lista[menor]:
                menor = i
            if lista[i] > lista[maior]:
                maior = i
        lista[i_ini], lista[menor] = lista[menor], lista[i_ini]
        if i_ini != maior:
            lista[i_fim-1], lista[maior] = lista[maior], lista[i_fim-1]
        resultado.append(copiar_lista(lista))
        i_ini += 1
        i_fim -= 1
        if i_ini >= i_fim-1: break
    return resultado

lista_baguncada = [7, 4, 8, 1, 2, 3]
#lista_baguncada = [7, 4, 2, 10, 3, 9]
#lista_baguncada = [10, 9,8,7,6,5,4,3,2,1]
#lista_baguncada = [2,3,3]
print(minmax_sort(lista_baguncada))

