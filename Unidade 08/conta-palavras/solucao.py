# (c) amiltoncristian9@gmail.com
# Creation Date: 26-04-2021
# Last Modified: seg 26 abr 2021 11:39:48
# Descobrir quantas palavras tem tamanho maior ou igual a K

def conta_palavras(k, palavras):
    tamanho, quantidade = 0, 0
    print(len(palavras))
    for i, caractere in enumerate(palavras):
        if caractere == ':' or i == len(palavras) -1:
            if tamanho >= k:
                quantidade += 1
            tamanho = 0
            continue
        tamanho += 1
    return quantidade


print(conta_palavras(5, "zero:um:dois:tres:quatro:cinco"))
