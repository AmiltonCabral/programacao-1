# (py) amiltoncristian9@gmail.com
# Date: 17/03/2021, Last Change: Never
# Imprimir a parte fracionária de um número

n_completo = float(input())

n_inteira = n_completo // n_completo
n_decimal = n_completo % n_inteira

print(f'{n_decimal:.1f}')
