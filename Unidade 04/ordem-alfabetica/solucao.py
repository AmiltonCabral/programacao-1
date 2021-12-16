# (py) amiltoncristian9@gmail.com
# Creation Date: 08-04-2021
# Last Modified: qui 08 abr 2021 09:22:54
# Classificar a ordem alfabética de uma palavra de referência

N = int(input())
sequencia = []

for i in range(N):
    sequencia += input().split()

print('---')

referencia = input()
antes = 0
depois = 0

for i in range(N):
    if referencia > sequencia[i]:
        antes += 1
    elif referencia < sequencia[i]:
        depois += 1

print(f'{antes} antes')
print(f'{depois} depois')
