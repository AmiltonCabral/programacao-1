# (py) amiltoncristian9@gmail.com
# Date: 23/03/2021, Last Change: Never
# Imprimir o quadrado de uma determinada sequência de números

x = int(input())
y = int(input())
n_condicao = (y - x) + 1
n_quadrado = x ** 2

if x > y:
    print('---')
else:
    for i in range(n_condicao):
        print(x, x**2 , sep=' ')
        x += 1
