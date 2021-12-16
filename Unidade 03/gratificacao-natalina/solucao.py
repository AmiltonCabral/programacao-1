# (py) amiltoncristian9@gmail.com
# Date: 22/03/2021, Last Change: Never
# Calcula quanto de bonificação cada cargo ganhará de acordo com
# suas faltas e cargo

n_codigo_cargo = int(input())

if n_codigo_cargo == 1:
    print('Deverá receber em dezembro R$ 25000.00.')

elif n_codigo_cargo == 2:
    print('Deverá receber em dezembro R$ 15000.00.')

elif n_codigo_cargo == 3:
    n_faltas = int(input())
    n_gratificacao = (235 - n_faltas) * 2
    print(f'Valor da gratificação R$ {n_gratificacao:.2f}.')
    print(f'Deverá receber em dezembro R$ 8000.00.')

elif n_codigo_cargo == 4:
    n_faltas = int(input())
    n_gratificacao = (235 - n_faltas) * 1
    print(f'Valor da gratificação R$ {n_gratificacao:.2f}.')
    print(f'Deverá receber em dezembro R$ 5000.00.')

elif n_codigo_cargo == 5:
    n_faltas = int(input())
    n_gratificacao = (235 - n_faltas) * 0.7
    print(f'Valor da gratificação R$ {n_gratificacao:.2f}.')
    print(f'Deverá receber em dezembro R$ 2800.00.')
