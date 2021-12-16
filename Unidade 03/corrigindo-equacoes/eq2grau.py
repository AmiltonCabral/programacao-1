# (py) amiltoncristian9@gmail.com
# Date: 24/03/2021, Last Change: Never
# Corrigir soluções, calculando raizes da equação de segundo grau

a = int(input())
b = int(input())
c = int(input())

delta = (b**2 - 4*a*c)
x1 = (-b + delta**(1/2)) / (2*a)
x2 = (-b - delta**(1/2)) / (2*a)

if delta < 0:
    print('sem raizes reais')

elif delta == 0:
    print(f'x = {x1:.2f}')

elif delta > 0:
    print(f'x1 = {x1:.2f}')
    print(f'x2 = {x2:.2f}')
