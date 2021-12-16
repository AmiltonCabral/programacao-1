# (c) amiltoncristian9@gmail.com
# Creation Date: 23-04-2021
# Last Modified: sex 23 abr 2021 14:41:36
# Criar um programa que embaralha cartas

def girar_esquerda(barai):
    barai_aux = []
    ultima_carta = barai.pop()
    while len(barai) > 0:
        barai_aux.append(barai.pop(0))
    barai.append(ultima_carta)
    for i in barai_aux:
        barai.append(i)


def girar_direita(barai):
    barai_aux = []
    primeira_carta = barai.pop(0)
    while len(barai) > 0:
        barai_aux.append(barai.pop(0))
    for i in barai_aux:
        barai.append(i)   
    barai.append(primeira_carta)


def intercalar(barai):
    for i in range(0, len(barai) -1, 2):
        barai[i], barai[i+1] = barai[i+1], barai[i]


baralho = input().split()
while True:
    comando = input()
    if comando == 'fim':
        break
    elif comando == 'GE':
        girar_esquerda(baralho)
    elif comando == 'GD':
        girar_direita(baralho)
    elif comando == 'I':
        intercalar(baralho)

    resultado = ''
    for i, item in enumerate(baralho):
        resultado += item
        if i == len(baralho)-1 : break
        resultado += ' '
    print(resultado)
