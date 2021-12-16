# (py) amiltoncristian9@gmail.com
# Date: 15/03/2021, Last Change: Never
# Descobrir a diferença da circunferência com o quadrado

import math

n_raio = float(input())

n_area_circulo = math.pi * n_raio ** 2
n_lado_quadrado = ((n_raio * 2) ** 2 / 2) ** 0.5
n_area_quadrado = n_lado_quadrado ** 2
n_area_incomum = n_area_circulo - n_area_quadrado

print(f'Área não comum: {n_area_incomum:.5f}')
