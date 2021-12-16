# (py) amiltoncristian9@gmail.com
# Date: , Last Change: Never
# 

a = [7, 4, 9, 64, 6, 1, 204, -5, 0, 2]
contador = 0
maior = 0
numero = a[0]
ordem = 0

for i in range(len(a)):
    numero = a[contador]
    contador += 1
    if maior < numero:
        maior = numero

for k in a:
    ordem += 1
    if k == maior:
        print(ordem)
