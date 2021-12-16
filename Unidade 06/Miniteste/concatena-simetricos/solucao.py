# (py) amiltoncristian9@gmail.com
# Creation Date: 15-04-2021
# Last Modified: qui 15 abr 2021 08:54:02
# Ajustar a ordem das palavras de forma simétrica

def concatena_simetricos(valores):
    novos_valores = []
    contador = len(valores) -1
    for i in range(len(valores) // 2 ):
        if valores[i][0] <= valores[contador][0]:
            novos_valores.append(valores[i] + valores[contador])
        else:
            novos_valores.append(valores[contador] + valores[i])
        contador -= 1
    if len(valores) % 2 == 1:
        novos_valores.append( valores[(len(valores) // 2)] )
    return novos_valores
