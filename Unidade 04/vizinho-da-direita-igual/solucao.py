# (py) amiltoncristian9@gmail.com
# Creation Date: 06-04-2021
# Last Modified: ter 06 abr 2021 15:34:30
# Conta quantas vezes o vizinho é igual ao elemento 

numeros = input().split()

contador = 0

for i in range(len(numeros) -1):
    if numeros[i] == numeros[i +1]:
        contador += 1

print(contador)
