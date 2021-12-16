# (py) amiltoncristian9@gmail.com
# Date: 09/04/2021, Last Change: 10:20 abr-09-2021 
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
