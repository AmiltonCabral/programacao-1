# (py) amiltoncristian9@gmail.com
# Creation Date: 10-04-2021
# Last Modified: sáb 10 abr 2021 21:19:10
# imprimir todos os múltiplos de 5, pares e positivos menores que um limite dado

lim = int(input())
mult = 2

while True:
    if 5 * mult >= lim: break

    print(5 * mult)
    mult += 2
