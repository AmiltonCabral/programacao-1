# (py) amiltoncristian9@gmail.com
# Date: 22/03/2021, Last Change: Never
# Descobrir a primeira vogal de uma palavra

palavra = input()
vogais = "AEIOUaeiou"
vogal = ""

for letra in palavra:
    if letra in vogais:
        vogal += letra
        break

if vogal == "":
    print('-')
else:
    print(vogal)
