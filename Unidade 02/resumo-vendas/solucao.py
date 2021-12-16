# (py) amiltoncristian9@gmail.com
# Date: 15/03/2021, Last Change: Never
# Relatório de vendas da loja por mês

n_loja = int(input())
n_teresa = int(input())
n_carla = int(input())

n_joaquim = n_loja - (n_teresa + n_carla)
n_media_teresa = n_teresa * 100 / n_loja
n_media_joaquim = n_joaquim * 100 / n_loja
n_media_carla = n_carla * 100 / n_loja

print(f'Teresa vendeu {n_teresa} (de {n_loja}) brinquedos. ({n_media_teresa:.2f}%)')
print(f'Joaquim vendeu {n_joaquim} (de {n_loja}) brinquedos. ({n_media_joaquim:.2f}%)')
print(f'Carla vendeu {n_carla} (de {n_loja}) brinquedos. ({n_media_carla:.2f}%)')
