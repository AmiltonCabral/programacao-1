# (py) amiltoncristian9@gmail.com
# Date: 02/04/2021, Last Change: Never
# Recebe um número com a altura da arvore e desenha ela

altura = int(input())
recuo = 1
folha = 1

for i in range(altura):
    print(" " * (altura -recuo), "o" * folha, sep='')
    recuo += 1
    folha += 2

print(" " *(altura -1), "o", sep='')
