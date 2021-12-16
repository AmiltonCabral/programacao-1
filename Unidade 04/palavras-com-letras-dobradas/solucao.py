# (py) amiltoncristian9@gmail.com
# Date: 30/03/2021, Last Change: Never
# Descobrir quais palavras possuem letras duplicadas

num_entrada = int(input())

lista_palavras = []
sem_letra_dobrada = []
com_letra_dobrada = []
lista_marcacao = []
contador = 0

# Lista palavras com letras dobradas
for i in range(num_entrada):
    lista_palavras.append(input())
    lista_marcacao.append(1)
    for j in range(int(len(lista_palavras[i]))-1):
        letra_atual = lista_palavras[i][j]
        letra_proxima = lista_palavras[i][j+1]
        if letra_atual == letra_proxima:
            com_letra_dobrada.append(lista_palavras[i])
            lista_marcacao[i] = 0
            break

# Lista palavras sem letras dobradas
for i in range(num_entrada):
    if lista_marcacao[contador] == 1:
        sem_letra_dobrada.append(lista_palavras[contador])
    contador += 1

num_com_dobrada = len(com_letra_dobrada)
num_sem_dobrada = len(sem_letra_dobrada)

print(f'{num_com_dobrada} palavra(s) com letras dobradas:')
for i in range(num_com_dobrada):
    print(com_letra_dobrada[i])
print('---')
print(f'{num_sem_dobrada} palavra(s) sem letras dobradas:')
for i in range(num_sem_dobrada):
    print(sem_letra_dobrada[i])
