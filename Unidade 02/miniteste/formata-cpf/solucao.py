# (py) amiltoncristian9@gmail.com
# Date: 17/03/2021, Last Change: Never
# Formatar CPF dos ganhadores e somar últimos digitos

n_cpf_1 = int(input())
n_cpf_2 = int(input())
n_cpf_3 = int(input())

n_ultimos_cpf_1 = n_cpf_1 % 100
n_ultimos_cpf_2 = n_cpf_2 % 100
n_ultimos_cpf_3 = n_cpf_3 % 100

n_primeiros_cpf_1 = n_cpf_1 // 100
n_primeiros_cpf_2 = n_cpf_2 // 100
n_primeiros_cpf_3 = n_cpf_3 // 100

n_penultimo_cpf_1 = n_ultimos_cpf_1 // 10
n_penultimo_cpf_2 = n_ultimos_cpf_2 // 10
n_penultimo_cpf_3 = n_ultimos_cpf_3 // 10

n_ultimo_cpf_1 = n_ultimos_cpf_1 % 10
n_ultimo_cpf_2 = n_ultimos_cpf_2 % 10
n_ultimo_cpf_3 = n_ultimos_cpf_3 % 10

n_soma_cpf_1 = n_penultimo_cpf_1 + n_ultimo_cpf_1
n_soma_cpf_2 = n_penultimo_cpf_2 + n_ultimo_cpf_2
n_soma_cpf_3 = n_penultimo_cpf_3 + n_ultimo_cpf_3

print(f'{n_primeiros_cpf_1}-{n_ultimos_cpf_1}')
print(n_soma_cpf_1)
print(f'{n_primeiros_cpf_2}-{n_ultimos_cpf_2}')
print(n_soma_cpf_2)
print(f'{n_primeiros_cpf_3}-{n_ultimos_cpf_3}')
print(n_soma_cpf_3)
