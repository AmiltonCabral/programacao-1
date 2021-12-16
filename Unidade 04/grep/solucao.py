# (py) amiltoncristian9@gmail.com
# Date: 30/03/2021, Last Change: Never
# Verificar se contém uma palavra especifica nas frases

chave = list(input())
n_frases = int(input())

contador = 0

for i in range(n_frases):
    frase = input()
    lista_frase = list(frase)
    for j in lista_frase:
        if chave[0:2] == lista_frase[contador:contador+2]:
            print(frase)
        contador += 1
    contador = 0
