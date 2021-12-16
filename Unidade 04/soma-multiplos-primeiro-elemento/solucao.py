# (py) amiltoncristian9@gmail.com
# Date: 02/04/2021, Last Change: Never
# Dado um numero de referência, soma os números primos a referência

inteiros = []
multiplo = []
resultado = 0

referencia = int(input())

for i in range(10):
    n = int(input())
    inteiros.append(n)

for i in inteiros:
    if i % referencia == 0:
        multiplo.append(i)

for i in multiplo:
    resultado = resultado + i

print(resultado)
