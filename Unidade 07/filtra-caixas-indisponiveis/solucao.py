# (c) amiltoncristian9@gmail.com
# Creation Date: 21-04-2021
# Last Modified: qua 21 abr 2021 18:43:20
# Tira itens da lista abaixo de um determinado valor

def filtra_caixas_indisponiveis(lista_caixas, qtd_itens):
    if len(lista_caixas) > 1:
        passa = True
    elif lista_caixas[0] < qtd_itens:
        lista_caixas.pop()
        passa = False
    else:
        passa = False

    while passa:
        if len(lista_caixas) <= 0: break
        for i, item in enumerate(lista_caixas):
            if item < qtd_itens:
                lista_caixas.pop(i)
                passa = True
                break
            passa = False


'''caixas = [2,1,3,1]
print(filtra_caixas_indisponiveis(caixas,5))
print(caixas)'''
