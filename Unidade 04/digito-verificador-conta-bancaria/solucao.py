# (py) amiltoncristian9@gmail.com
# Creation Date: 06-04-2021
# Last Modified: ter 06 abr 2021 17:13:21
# Calcular digito verificador da conta 

num_conta = input()

soma = 0

for i in num_conta:
    soma += int(i)

digito = soma % 11

if digito == 10:
    digito = 'X'

print(f'{num_conta}-{digito}')
