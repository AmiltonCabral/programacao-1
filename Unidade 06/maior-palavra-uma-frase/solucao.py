# (py) amiltoncristian9@gmail.com
# Creation Date: 14-04-2021
# Last Modified: qua 14 abr 2021 21:00:59
# Dizer qual a maior palavra

def maior_palavra(frase):
    palavra = ''
    maior_palavra = ''
    for i in frase:
        if i != ' ':
            palavra += i
        if len(palavra) >= len(maior_palavra):
            maior_palavra = palavra
        if i == ' ':
            palavra = ''
    return maior_palavra
