# (c) amiltoncristian9@gmail.com
# Creation Date: 26-04-2021
# Last Modified: seg 26 abr 2021 16:36:34
# Reverter elementos de uma lista em um determinado range

def flip(lista, i, j):
    parada = len(list(range(i, j+1))) // 2
    for _ in range(parada):
        lista[i], lista[j] = lista[j], lista[i]
        i += 1
        j -= 1


'''array = [1, 2, 3, 4, 5, 6, 7]
flip(array, 2, 6)
print(array)'''
