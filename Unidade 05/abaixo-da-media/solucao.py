# (py) amiltoncristian9@gmail.com
# Creation Date: 12-04-2021
# Last Modified: seg 12 abr 2021 08:18:26
# Imprimi a média de números e quais estão abaixo dela

seq, soma = [], 0

while True:
    next_value = input()
    if next_value == 'fim': break
    seq.append(int(next_value))
    soma += int(next_value)
    media = soma / len(seq)

print(f'{media:.2f}')

for i in range(len(seq)):
    if seq[i] < media:
        print(f'{i+1} {seq[i]}')
