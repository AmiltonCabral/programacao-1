# (py) amiltoncristian9@gmail.com
# Date: 17/03/2021, Last Change: Never
# Quantidade necessária de tinta para pintar uma parede

n_altura = float(input())
n_largura = float(input())

n_area_parede = n_altura * n_largura
n_resultado = (3.6 * n_area_parede) / 50

print(f'{n_resultado:.2f} l')
