# (py) amiltoncristian9@gmail.com
# Creation Date: 12-04-2021
# Last Modified: seg 12 abr 2021 22:39:08
# Conta quantos votos sim e nao teve em uma lista

def conta_votos(lista, id_votacao):
    sim, nao = 0, 0
    for i in range(len(lista)):
        voto_atual = lista[i].split(',')
        if voto_atual[2] == str(id_votacao):
            if voto_atual[1] == 'sim':
                sim += 1
            elif voto_atual[1] == 'nao':
                nao += 1
    return [sim,nao]
