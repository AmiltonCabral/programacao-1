# (py) amiltoncristian9@gmail.com
# Creation Date: 06-04-2021
# Last Modified: ter 06 abr 2021 11:16:39
# Descobrir onde está as letras na frase

frase = input()
chave = input()
somador = 0
out = ''

for i in chave:
    for j in frase:
        if j == i:
            if out == '':
                out += str(somador)
            else:
                out += ' ' + str(somador)
        somador += 1
    if out == '':
        print('-1')
    else:
        print(out)
    somador = 0
    out = ''
