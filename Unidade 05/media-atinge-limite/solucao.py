# (py) amiltoncristian9@gmail.com
# Creation Date: 12-04-2021
# Last Modified: seg 12 abr 2021 08:33:47
# Informar quando os números atinge a média máxima desejada

valores, soma = [], 0

while True:
    next_value = input()
    if next_value == '-': break
    valores.append(float(next_value))

media_max = float(input())

for i in range(len(valores)):
    soma += valores[i]
    media_provisoria = soma / (i +1)
    if media_provisoria >= media_max:
        print(f'media = {media_provisoria:.1f}')
        print(f'num = {i +1}')
        break
