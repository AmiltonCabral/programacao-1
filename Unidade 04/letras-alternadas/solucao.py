# (py) amiltoncristian9@gmail.com
# Date: 31/03/2021, Last Change: Never
# Imprimir as letras alternadas de uma palavra

palavra = input()
count = 0
saida = []
str_saida = ''

for i in range( (len(palavra) +1) //2):
    saida.append(palavra[count])
    count += 2

for i in saida:
    str_saida += i

print(str_saida)
