# (py) amiltoncristian9@gmail.com
# Creation Date: 20-04-2021
# Last Modified: ter 20 abr 2021 12:11:21
# Remove a(s) palavra(s) que possuem mais vogais em uma lista

def remove_palavras_com_mais_vogais(lista):
    mais_vogais, vogais = 0, 0
    for palavra in lista:
        for letra in palavra:
            if letra in 'aeiouAEIOU':
                vogais += 1
        if vogais > mais_vogais:
            mais_vogais = vogais
        vogais = 0
    
    if mais_vogais > 1:
        continua = True
    else:
        continua = False
   
    while continua == True:
        indice, vogais, continua = 0, 0, False
        for palavra in lista:
            for letra in palavra:
                if letra in 'aeiouAEIOU':
                    vogais += 1
            if vogais >= mais_vogais:
                lista.pop(indice)
                continua = True
                break
            vogais = 0
            indice += 1
