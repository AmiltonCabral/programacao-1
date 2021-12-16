# (py) amiltoncristian9@gmail.com
# Date: 24/03/2021, Last Change: Never
# Descreve o segundo maior número e o segundo menor número entre quatro

a = int(input())
b = int(input())
c = int(input())
d = int(input())

print(f'Considerando os números {a}, {b}, {c} e {d}')

if a < b and a < c and a < d:
    a = 0
elif b < a and b < c and b < d:
    b = 0
elif c < a and c < b and c < d:
    c = 0
else:
    d = 0

if a > b and a > c and a > d:
    a = 0
elif b > a and b > c and b > d:
    b = 0
elif c > a and c > b and c > d:
    c = 0
else:
    d = 0

if a > b and a > c and a > d:
    maior = a
elif b > a and b > c and b > d:
    maior = b
elif c > a and c > b and c > d:
    maior = c
else:
    maior = d

#menor = (a + b + c + d) - maior
print(a, b, c, d)

print(f'O segundo menor número é {menor}')
print(f'O segundo maior número é {maior}')
