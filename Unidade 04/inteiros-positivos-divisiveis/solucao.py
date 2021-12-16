# (py) amiltoncristian9@gmail.com
# Creation Date: 06-04-2021
# Last Modified: ter 06 abr 2021 16:18:13
# Imprimi todos os inteiros divisíveis por determinado número

A = int(input())
B = int(input())
K = int(input())

for i in range(1, K+1):
    if i % A == 0 and i % B == 0:
        print(i)
