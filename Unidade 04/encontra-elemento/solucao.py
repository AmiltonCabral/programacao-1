# (py) amiltoncristian9@gmail.com
# Date: 31/03/2021, Last Change: Never
# Verificar se um número esta em uma lista de inteiros

N = input()
sequencia = input()
list_sequencia = sequencia.split()
resultado = 'não'

for i in list_sequencia:
    if i == N:
        resultado = 'sim'

print(resultado)
