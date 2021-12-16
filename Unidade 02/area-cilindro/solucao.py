# (py) amiltoncristian9@gmail.com
# Date: 17/03/2021, Last Change: Never
# Recebe diametro e altura do cilindro e devolve a superfície

import math

print('Cálculo da Superfície de um Cilindro')
print('---')
n_diametro = float(input('Medida do diâmetro? '))
n_altura = float(input('Medida da altura? '))
print('---')

n_raio = n_diametro / 2
n_area_base = math.pi * n_raio ** 2
n_perimetro = 2 * math.pi * n_raio
n_area_retangulo = n_altura * n_perimetro 
n_area_cilindro = n_area_retangulo + n_area_base * 2

print(f'Área calculada: {n_area_cilindro:.2f}')
