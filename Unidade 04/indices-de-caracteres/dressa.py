# (py) amiltoncristian9@gmail.com
# Creation Date: 06-04-2021
# Last Modified: ter 06 abr 2021 15:03:58
# 

frase = input().lower()
chave = input().lower()

for j in range(len(chave)):
    lista = ''
    for i in range(len(frase)):
            if chave[j] == frase[i]:
                lista += (f'{i}')

    for elemento in lista:
        if elemento == lista[-1]:
            print(f'{elemento}')
        else:
            print(f'{elemento}',end = ' ')

    if lista == '' :
        print('-1')
