# (c) amiltoncristian9@gmail.com
# Creation Date: 21-04-2021
# Last Modified: qua 21 abr 2021 15:55:07
# Remove da lista números que não for divisível pelo somatório dos algarismos que o compõem

def filtra_divisores(lista):
    repeticoes = len(lista)
    for _ in range(repeticoes):
        for i_lista, numero in enumerate(lista):
            soma = 0
            for algarismo in str(numero):
                soma += int(algarismo)
            if numero % soma != 0:
                lista.pop(i_lista)
                break
    

'''lista1 = [333, 121, 81]
print(filtra_divisores(lista1))
print(lista1)'''
