# (py) amiltoncristian9@gmail.com
# Date: 17/03/2021, Last Change: Never
# Calcular número de diagonais de um polígono

n_lados = float(input())

n_comeco_resultado = n_lados - 3
n_fim_resultado = n_lados / 2
n_resultado = n_comeco_resultado * n_fim_resultado

print(f'{n_lados:.0f} lados => {n_resultado:.0f} diagonais')
