# (py) amiltoncristian9@gmail.com
# Date: 01/04/2021, Last Change: 02/04/2021
# Dado um número, imprime sua posição em uma sequência

v = input()
valores = input()
lista_valores = valores.split()
resultado = []
contador = 0
resposta = '-1'

for i in lista_valores:
    if i == v:
        resultado.append(contador)
        resultado.append(" ")
    contador += 1

if resultado != []:
    resposta = ''
    contador = 0
    for i in resultado:
        resposta = resposta + str(i)
        contador += 1
        if contador == len(resultado) -1:
            break

print(resposta)
