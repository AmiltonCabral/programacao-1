# (py) amiltoncristian9@gmail.com
# Creation Date: 15-04-2021
# Last Modified: qui 15 abr 2021 09:11:16
# Entregar as sílabas das palavras apenas se a primeira letra for consoante e a segunda vogal

def quase_fonemas(palavra):
    resultado = []
    vogais = 'aeiou'
    for i in range(len(palavra) -1):
        if palavra[i] not in vogais and palavra[i+1] in vogais:
            resultado.append(palavra[i] + palavra[i+1])
    return resultado
