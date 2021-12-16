# (c) amiltoncristian9@gmail.com
# Creation Date: 23-04-2021
# Last Modified: sex 23 abr 2021 15:09:28
# Informar qual item aparece em mais da metade da lista

def lanchemaispedido(pedidos):
    mais_frequente = None
    for lanche1 in pedidos:
        repetido = 0
        for lanche2 in pedidos:
            if lanche1 == lanche2:
                repetido += 1
        if repetido > len(pedidos) // 2:
            mais_frequente = lanche1
    return mais_frequente


'''ines = ['tapioca','tapioca','salada','bolo','misto','tapioca', 'tapioca']
marcos = ['suco','coxinha','suco','misto','folhado']
print( lanchemaispedido(marcos) )'''
