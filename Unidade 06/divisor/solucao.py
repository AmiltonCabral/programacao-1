# (py) amiltoncristian9@gmail.com
# Creation Date: 14-04-2021
# Last Modified: qua 14 abr 2021 15:34:01
# Informa qual o índice do primeiro número da lista divisível pelo número escolhido

def divisor(num, lista):
    divisivel = -1
    for i in range(len(lista)):
        if lista[i] % num == 0:
            divisivel = i
            break
    return divisivel
