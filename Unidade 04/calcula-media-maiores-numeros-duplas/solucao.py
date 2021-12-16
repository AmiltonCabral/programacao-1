# (py) amiltoncristian9@gmail.com
# Creation Date: 08-04-2021
# Last Modified: qui 08 abr 2021 22:24:43
# Calcula a média dos maiores números das duplas

N = int(input())
soma = 0
mais = 0

for i in range(N):
    seq = input().split()
    if seq[0] > seq[1]:
        soma += int(seq[0])
        mais += 1
    elif seq[0] < seq[1]:
        soma += int(seq[1])
    else:
        N -= 1

if N == 0:
    print('Não é possível calcular a média.')
else:
    media = soma / N
    print(f'{media:.2f}')
