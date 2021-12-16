# (c) amiltoncristian9@gmail.com
# Creation Date: 23-04-2021
# Last Modified: sex 23 abr 2021 16:52:31
# Calcular medias

def media_aritimetica(valores):
    soma = 0
    for i in valores:
        soma += float(i)
    resultado = soma / len(valores)
    return f'{resultado:.4f}'


def media_geometrica(valores):
    produto = 1
    for i in valores:
        produto *= float(i)
    resultado = produto ** (1 / len(valores))
    return f'{resultado:.4f}'


def media_harmonica(valores):
    soma_a = 0
    for i in valores:
        soma_a += (1 / float(i))
    resultado = len(valores) / soma_a
    return f'{resultado:.4f}'


while True:
    comando = []
    comando += input().split()
    if comando[0] == 'Q': break
    lista_numeros = input().split()
    for i in comando:
        if i == 'MA':
            resultado = media_aritimetica(lista_numeros)
            print(f'Média Aritmética: {resultado}')
        elif i == 'MG':
            resultado = media_geometrica(lista_numeros)
            print(f'Média Geométrica: {resultado}')
        elif i == 'MH':
            resultado = media_harmonica(lista_numeros)
            print(f'Média Harmônica: {resultado}')
    print('----')
