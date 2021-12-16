# (py) amiltoncristian9@gmail.com
# Date: 31/03/2021, Last Change: Never
# Forma uma nova palavra a partir das letras mais pesadas de outras 3 palavras

palavra_1 = input()
palavra_2 = input()
palavra_3 = input()
palavra_1_2 = ''
nova_palavra = ''
count = 0

for i in palavra_1:
    if i > palavra_2[count]:
        palavra_1_2 += i
    else:
        palavra_1_2 += palavra_2[count]
    count += 1

count = 0

for i in palavra_3:
    if i > palavra_1_2[count]:
        nova_palavra += i
    else:
        nova_palavra += palavra_1_2[count]
    count += 1

print(nova_palavra)
