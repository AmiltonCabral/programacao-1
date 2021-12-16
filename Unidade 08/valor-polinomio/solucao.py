# (c) amiltoncristian9@gmail.com
# Creation Date: 26-04-2021
# Last Modified: qua 28 abr 2021 19:39:11
# Calcular o valor com um polinômio

def valor_polinomio(polinomio, valor):
    resposta = 0
    for grau in range(len(polinomio)):
        resposta += polinomio[grau] * valor ** grau
    return resposta
