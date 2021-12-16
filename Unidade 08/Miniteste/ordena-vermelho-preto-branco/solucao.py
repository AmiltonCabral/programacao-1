# (c) amiltoncristian9@gmail.com
# Creation Date: 29-04-2021
# Last Modified: qui 29 abr 2021 09:24:20
# Ordenar itens da lista

def ordena_vpb(lista):
    "v, p, b"
    acabou = False
    while not acabou:
        if len(lista) < 2: break
        for i in range(len(lista) -1):
            if lista[i] != 'v' and lista[i+1] == 'v':
                lista[i], lista[i+1] = lista[i+1], lista[i]
                acabou = False
                break
            acabou = True
    acabou = False
    while not acabou:
        if len(lista) < 2: break
        for i in range(len(lista) -1, 0, -1):
            print(i)
            if lista[i] != 'b' and lista[i-1] == 'b':
                lista[i], lista[i-1] = lista[i-1], lista[i]
                acabou = False
                break
            acabou = True


'''l = ['b', 'v', 'v', 'p', 'b', 'v', 'b']
l2 = ['p', 'b', 'v']
l3 = ['p']
ordena_vpb(l3)
print(l3)'''
