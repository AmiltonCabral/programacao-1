# (py) amiltoncristian9@gmail.com
# Date: 15/03/2021, Last Change: Never
# - A partir do lado do quadrado na circunferência,
#   calcula o perímetro e área da circunferência

import math

n_lado_quadrado = float(input())

n_metade_lado = n_lado_quadrado / 2
n_raio = (n_metade_lado ** 2 * 2) ** 0.5
n_perimetro = 2 * math.pi * n_raio
n_area = math.pi * n_raio ** 2

print(f'Perímetro: {n_perimetro:.5f}')
print(f'Área: {n_area:.5f}')
