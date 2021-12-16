# (py) amiltoncristian9@gmail.com
# Date: 23/03/2021, Last Change: Never
# Imprimir tabela dos senos e cossenos a partir do angulo, delta e linhas da tabela

import math

n_angulo = float(input())
n_delta = float(input())
n_linhas = int(input())
n_rad = n_angulo * math.pi / 180
n_seno = math.sin(n_rad)
n_cos = math.cos(n_rad)
print("|Angulo|   Seno|Cosseno|")

for i in range(n_linhas):
    print(f'|{n_angulo:>6}|{n_seno:.5f}|{n_cos:.5f}|')
    n_angulo += n_delta
    n_rad = n_angulo * math.pi / 180
    n_seno = math.sin(n_rad)
    n_cos = math.cos(n_rad)
