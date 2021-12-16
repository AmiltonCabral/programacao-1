# (c) amiltoncristian9@gmail.com
# Creation Date: 22-04-2021
# Last Modified: qui 22 abr 2021 09:07:23
# Substitui elementos da lista de acordo com regras

def remove_mantem_modifica(lista):
    i = 0
    while i < len(lista):
        if lista[i] % 3 == 0 and lista[i] % 4 == 0 and lista[i] % 5 == 0:
            lista[i] = 60
            i += 1
        elif lista[i] % 3 == 0 and lista[i] % 4 == 0:
            lista[i] = 12
            i += 1
        elif lista[i] % 4 == 0 and lista[i] % 5 == 0:
            lista[i] = 20
            i += 1
        elif lista[i] % 3 == 0 and lista[i] % 4 != 0 and lista[i] % 5 != 0:
            lista.pop(i)
        elif lista[i] % 3 != 0 and lista[i] % 4 == 0 and lista[i] % 5 != 0:
            lista.pop(i)
        elif lista[i] % 3 != 0 and lista[i] % 4 != 0 and lista[i] % 5 == 0:
            lista.pop(i)
        else:
            i += 1
            continue


'''l1 = [1, 2, 3, 120, 24]
l2 = [10, 20, 24, 31]
print(remove_mantem_modifica(l2))
print(l2)'''
