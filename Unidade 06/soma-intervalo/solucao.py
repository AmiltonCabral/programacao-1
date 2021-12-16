# (py) amiltoncristian9@gmail.com
# Creation Date: 12-04-2021
# Last Modified: seg 12 abr 2021 21:16:48
# A partir de dois valores, soma todos os números entre esses valores e retorna

def soma_intervalo(a, b):
    soma = 0
    for i in range(a, b+1):
        soma += i
    return soma
