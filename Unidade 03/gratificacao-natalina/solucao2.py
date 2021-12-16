# (py) amiltoncristian9@gmail.com
# Date: 22/03/2021, Last Change: Never
# Calcula quanto de bonificação cada funcionário ganhará de acordo
# [...] com suas faltas e seu cargo.

n_codigo = int(input())
n_faltas = -1

if n_codigo == 1:
    n_salario = 25000

elif n_codigo == 2:
    n_salario = 15000

elif n_codigo == 3:
    n_salario = 8000
    n_faltas = int(input())
    n_grat_total = 500
    n_grat_dia = 2

elif n_codigo == 4:
    n_salario = 5000
    n_faltas = int(input())
    n_grat_total = 300
    n_grat_dia = 1

else:
    n_salario = 2800
    n_faltas = int(input())
    n_grat_total = 200
    n_grat_dia = 0.7

# ---- print com resultados ----

if n_faltas < 0:
    print(f'Deverá receber em dezembro R$ {n_salario:.2f}.')

elif n_faltas == 0:
    print(f'Valor da gratificação R$ {n_grat_total:.2f}.')
    n_salario_final = n_salario + n_grat_total
    print(f'Deverá receber em dezembro R$ {n_salario_final:.2f}.')

else:
    n_gratificacao = (235 - n_faltas) * n_grat_dia
    print(f'Valor da gratificação R$ {n_gratificacao:.2f}.')
    n_salario_final = n_salario + n_gratificacao
    print(f'Deverá receber em dezembro R$ {n_salario_final:.2f}.')
