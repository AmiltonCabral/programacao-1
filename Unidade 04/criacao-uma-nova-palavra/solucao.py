# (py) amiltoncristian9@gmail.com
# Date: 01/04/2021, Last Change: Never
# Criar uma palavra nova, repetindo as letras de acordo com o numero informado

palavra = input()
num = input()
nova_palavra = ''
contador = len(palavra) -1

for i in palavra:
    nova_palavra += i
    nova_palavra += (i * int(num[contador]))
    contador -= 1

print(nova_palavra)
