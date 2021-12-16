# (py) amiltoncristian9@gmail.com
# Creation Date: 08-04-2021
# Last Modified: qui 08 abr 2021 22:09:35
# Recebe palavras e conta até receber uma com mais consoantes que vogais

consoante = 0
vogal = 0
entradas = 0

while consoante <= vogal:
    consoante = 0
    vogal = 0
    palavra = input().lower()
    for i in palavra:
        if i in 'aeiou':
            vogal += 1
        else:
            consoante += 1
    entradas += 1

print(entradas)
