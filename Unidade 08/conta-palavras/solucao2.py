# (c) amiltoncristian9@gmail.com
# Creation Date: 26-04-2021
# Last Modified: qua 28 abr 2021 08:59:30
# Descobrir quantas palavras tem tamanho maior ou igual a K

def conta_palavras(k, palavras):
    lista_palavras = palavras.split(':')
    quantidade = 0
    for palavra in lista_palavras:
        if k == 0 and palavra == '':
            quantidade += 1
        for i in range(len(palavra)):
            if i+1 >= k:
                quantidade += 1
                break
    return quantidade


#print(conta_palavras(0, "zero:um:dois:tres:quatro:cinco::casa"))
#print(conta_palavras(0, "io::oi"))
