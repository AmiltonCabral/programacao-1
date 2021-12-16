# (c) amiltoncristian9@gmail.com
# Creation Date: 21-04-2021
# Last Modified: qua 21 abr 2021 09:48:54
# Verifica se a ordem de uma esteira esta correta

def verifica_esteira(l1, l2):
    i_1 = 0
    confimacao = 0
    for item_2 in l2:
        if i_1 + 1 >= len(l1): break
        while True:
            if i_1 >= len(l1): break
            if item_2 == l1[i_1]:
                confimacao += 1
                i_1 += 1
                break
            i_1 += 1
    if confimacao >= len(l2):
        return True
    else:
        return False
