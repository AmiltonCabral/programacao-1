# (py) amiltoncristian9@gmail.com
# Creation Date: 14-04-2021
# Last Modified: dom 18 abr 2021 20:04:25
# Resumir uma lista com operações

def soma_diminui_vizinhos(lista):
    resultado = 0
    if len(lista) == 0: return 0
    else:
        numero_1 = lista.pop(0)
        resultado = numero_1
    for _ in range(10): #Esse 10 nao é magico, deve ser suficiente para calcular toda a lista
        if len(lista) == 0:
            resultado = numero_1
            break
        numero_2 = lista.pop(0)
        soma = numero_1 + numero_2
        if len(lista) == 0:
            resultado = soma
            break
        numero_3 = lista.pop(0)
        numero_1 = soma - numero_3
    return resultado

print( soma_diminui_vizinhos([1, 2, 3, 4, 3]) )
