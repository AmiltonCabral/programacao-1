# (py) amiltoncristian9@gmail.com
# Date: 02/04/2021, Last Change: Never
# Descobrir quantos números são pares e ímpares

n = int(input())
inteiros = []
par = 0
soma_par = 0
impar = 0
soma_impar = 0

for i in range(n):
    inteiros.append( int(input()))

for i in inteiros:
    if i % 2 == 0:
        par += 1
        soma_par += i
    else:
        impar += 1
        soma_impar += i

media_par = soma_par / par
media_impar = soma_impar / impar

print(f'pares: {par}')
print(f'ímpares: {impar}')
print(f'média pares: {media_par:.1f}')
print(f'média ímpares: {media_impar:.1f}')
