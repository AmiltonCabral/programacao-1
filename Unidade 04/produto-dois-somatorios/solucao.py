# (py) amiltoncristian9@gmail.com
# Date: 03/04/2021, Last Change: Never
# Soma os números das posições pares e multiplica com os números das posições ímpares

num = input()

sum_par = int(num[0]) + int(num[2]) + int(num[4])
sum_impar = int(num[1]) + int(num[3])
produto = sum_par * sum_impar

print(f'{produto:05d}')
