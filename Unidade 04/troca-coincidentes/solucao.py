# (py) amiltoncristian9@gmail.com
# Date: 03/04/2021, Last Change: Never
# Decodificar uma frase com a chave de acordo com sua posição dada

frase = list(input())
chave = input()
n = 0

for i in frase:
    if i == '0':
        frase[n] = chave[0]
    elif i == '1':
        frase[n] = chave[1]
    elif i == '2':
        frase[n] = chave[2]
    elif i == '3':
        frase[n] = chave[3]
    elif i == '4':
        frase[n] = chave[4]
    elif i == '5':
        frase[n] = chave[5]
    elif i == '6':
        frase[n] = chave[6]
    elif i == '7':
        frase[n] = chave[7]
    elif i == '8':
        frase[n] = chave[8]
    elif i == '9':
        frase[n] = chave[9]
    n += 1

print(frase)
