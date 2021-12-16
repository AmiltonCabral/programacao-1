# (py) amiltoncristian9@gmail.com
# Creation Date: 07-04-2021
# Last Modified: qua 07 abr 2021 19:25:13
# Lê duas palavras e diz onde tem letras comuns e quantas

palavra_1 = input()
palavra_2 = input()

print('Letras coincidentes')

coincidentes = 0

for i in range(len(palavra_1)):
    if palavra_1[i] == palavra_2[i]:
        coincidentes += 1
        print(f"'{palavra_1[i]}' na posição {i + 1}")

por_cem = coincidentes * 100 / (len(palavra_1) + len(palavra_2))

print(f'Total de letras coincidentes: {coincidentes} ({por_cem:.0f}%)')
