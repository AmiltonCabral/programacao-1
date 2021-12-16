# (py) amiltoncristian9@gmail.com
# Creation Date: 12-04-2021
# Last Modified: seg 12 abr 2021 11:13:06
# Faz a média do tamanho das palavras lidas, imprime a média e as palavras acima da média

lista_palavras, soma_palavras, contagem = [], 0, 0

while True:
    next_palavra = input()
    if next_palavra == 'fim': break    
    lista_palavras.append(next_palavra)
    soma_palavras += len(next_palavra)
    contagem += 1

media = soma_palavras / contagem
print(f'{media:.2f}')

for i in range(len(lista_palavras)):
    if len(lista_palavras[i]) > media:
        print(f'{i+1} {lista_palavras[i]}')

