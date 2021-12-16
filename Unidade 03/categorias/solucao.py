# (py) amiltoncristian9@gmail.com
# Date: 24/03/2021, Last Change: Never
# Recebe a idade do nadador e diz sua categoria

nome = input()
n_idade = int(input())

if n_idade < 5:
    print(f'{nome}, {n_idade} anos, Não pode competir.')

elif 5 <= n_idade <= 7:
    print(f'{nome}, {n_idade} anos, Infantil A.')

elif 8 <= n_idade <= 10:
    print(f'{nome}, {n_idade} anos, Infantil B.')

elif 11 <= n_idade <= 13:
    print(f'{nome}, {n_idade} anos, Juvenil A.')

elif 14 <= n_idade <= 17:
    print(f'{nome}, {n_idade} anos, Juvenil B.')

else:
    print(f'{nome}, {n_idade} anos, Senior.')
