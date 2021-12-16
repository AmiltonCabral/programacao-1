# (c) amiltoncristian9@gmail.com
# Creation Date: 20-05-2021
# Last Modified: Thu 20 May 2021 09:44:28 -03
# 

tabela_quimica = {'H':1, 'S':32, 'O':16, 'C':12, 'Ca':40, 'Na':23, 'P':31}
saida = []

def soma_atomos(tabela, entrada):
    soma = 0
    tem_digito = False
    for i in range(len(entrada) -1, -1, -1):
        if entrada[i].isdigit():
            tem_digito = True
            digito = entrada[i]
            continue
        if tem_digito:
            soma += tabela_quimica[entrada[i]] * int(digito)
            tem_digito = False
            continue

        soma += tabela_quimica[entrada[i]]
        tem_digito = False

    return soma


while True:
    entrada = input().split()
    if entrada == ['fim']: break
    saida.append(soma_atomos(tabela_quimica, entrada))

for item in saida:
    print(item)
