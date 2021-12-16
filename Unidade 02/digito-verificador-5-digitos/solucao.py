# (py) amiltoncristian9@gmail.com
# Date: 16/03/2021, Last Change: Never
# Cria número verificador de conta corrente

n_conta = input()

n_int_conta = list(map(int, str(n_conta)))
n_soma_conta = sum(n_int_conta)
n_verificador = n_soma_conta % 11

print(f'{n_conta}-{n_verificador:02d}')
