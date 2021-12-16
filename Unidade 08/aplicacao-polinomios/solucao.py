# (c) amiltoncristian9@gmail.com
# Creation Date: 28-04-2021
# Last Modified: qua 28 abr 2021 20:05:12
# Calcular polinomios

def valor_polinomio(polinomio, valor):
    resposta = 0
    for grau in range(len(polinomio)):
        resposta += int(polinomio[grau]) * int(valor[0]) ** grau
    return resposta


saida = []
while True:
    entrada = input()
    if entrada == 'fim': break
    entrada = entrada.split()

    if entrada[0] == 'p:':
        saida.append('novo polinomio')
        polinomio = []
        polinomio += entrada
        polinomio.pop(0)
    else:
        saida.append(valor_polinomio(polinomio, entrada))

for i in saida:
    print(i)
