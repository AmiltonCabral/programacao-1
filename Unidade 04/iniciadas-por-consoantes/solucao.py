# (py) amiltoncristian9@gmail.com
# Date: 22/03/2021, Last Change: Never
# Descobre quantas palavras são iniciadas por consoantes e sua porcentagem 

n_palavras = int(input())
consoantes = "bcdfghjklmnpqrstvwxyz"
lista_palavras = []
n_inicia_consoante = 0


for i in range(n_palavras):
    lista_palavras.append(input())

for j in range(n_palavras):
    if (lista_palavras[j][0]) in consoantes:
        n_inicia_consoante += 1

n_porcentagem = (100 * n_inicia_consoante) / n_palavras

print(f'total de palavras: {n_palavras}')
print(f'iniciadas por consoantes: {n_inicia_consoante} ({n_porcentagem:.2f}%)')

