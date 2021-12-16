# (c) amiltoncristian9@gmail.com
# Creation Date: 26-04-2021
# Last Modified: seg 26 abr 2021 12:36:19
# A partir de um pivot e uma sequência de números, separar os maiores e os menores do pivot

pivot = int(input())
entrada = 0
maiores, menores = [], []

while True:
    entrada = int(input())
    if entrada < 0: break
    if entrada > pivot:
        maiores.append(entrada)
    elif entrada <= pivot:
        menores.append(entrada)

print(menores)
print(pivot)
print(maiores)
