# Uma Variação do Método Noves Fora
# (c) 2021-04-20, ivyna.rufino@ccc.ufcg.edu.br

def meu_slice(lista, ini, fim):
    nova_lista = []
    for i in range(ini, fim):
        nova_lista.append(lista[i])
    return nova_lista


def lista_decrescente(lista):
    tamanho = len(lista)
    nova_lista = []
    while len(nova_lista) < tamanho:
        maior = lista[0]
        indice = 0
        for i in range(len(lista)):
            if lista[i] > maior:
                maior = lista[i]
                indice = i
            else:
                maior = maior
        lista.pop(indice)
        nova_lista.append(maior)
    return nova_lista


def noves_fora(lista):
    evolucao = [lista]
    resta = 0
    if len(lista) == 1:
        if lista[0] < 9:
            resta = lista[0]
            return f"({resta}, {evolucao})"
        else:
            evolucao.append([0])
            return f"({resta}, {evolucao})"
    i = 0
    while True:
        if len(lista) == 1:
            if lista[0] < 9: break
            else:
                evolucao[1] = [0]
                resta = 0
                break
        resta = lista[0] + lista[1]
        if resta >= 9:
            resta -= 9
        lista = [resta] + meu_slice(lista, 2, len(lista))
        lista = lista_decrescente(lista)
        evolucao.append(lista)
        i += 1

#    print(resta, evolucao)
#    return f"({resta}, {evolucao})"
    return [resta, evolucao]


print( noves_fora([9, 9, 1]) )



