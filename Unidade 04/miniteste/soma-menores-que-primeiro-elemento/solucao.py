# (py) amiltoncristian9@gmail.com
# Creation Date: 12-04-2021
# Last Modified: seg 12 abr 2021 10:45:38
# A partir de um número de referência, conta quantos são menores e os soma

n_referencia = int(input())
menores, contagem = 0, 0

for i in range(10):
    next_num = int(input())
    if next_num < n_referencia:
        menores += next_num
        contagem += 1

print(f'menores = {contagem}')
print(f'soma = {menores}')
