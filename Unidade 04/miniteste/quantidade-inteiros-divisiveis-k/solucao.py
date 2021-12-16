# (py) amiltoncristian9@gmail.com
# Date: 25/03/2021, Last Change: Never
# Descobre quantos números são divisíveis por K 

k = int(input())
n = int(input())
divisiveis = 0

for i in range(n):
    n_sequencia = int(input())
    n_resto = n_sequencia % k
    if n_resto == 0:
        divisiveis += 1

porcentagem = (divisiveis * 100) / n

print(f'{divisiveis} ({porcentagem:.1f}%)')
