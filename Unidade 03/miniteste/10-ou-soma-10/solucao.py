# (py) amiltoncristian9@gmail.com
# Date: 25/03/2021, Last Change: Never
# Recebe dois números e responde se o valor de pelo menos um deles é 10 ou a soma deles é 10

n_a = int(input())
n_b = int(input())

if n_a == 10 or n_b == 10 or n_a + n_b == 10:
    resultado = 'SIM'
else:
    resultado = 'NAO'

print(resultado)
