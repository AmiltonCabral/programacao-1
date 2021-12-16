# (py) amiltoncristian9@gmail.com
# Creation Date: 12-04-2021
# Last Modified: seg 12 abr 2021 10:59:00
# Descobrir quantas senhas tem caracteres adjacentes iguais

N = int(input())
senhas, com = [], 0

for i in range(N):
    senhas.append(input())
    for j in range(len(senhas[i]) -1):
        if senhas[i][j] == senhas[i][j +1]:
            com += 1
            break

sem = N - com

print(f'com: {com}')
print(f'sem: {sem}')
