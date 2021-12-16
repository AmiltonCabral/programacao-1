# (py) amiltoncristian9@gmail.com
# Date: 03/04/2021, Last Change: Never
# Soma os números das posições pares e multiplica com os números das posições ímpares

num = input()
par = 0
impar = 0
contador = 0

for i in num:
    if contador % 2 == 0:
        par += int(i)
    else:
        impar += int(i)
    contador += 1

produto = par * impar

print(f'{produto:05d}')
