# (c) amiltoncristian9@gmail.com
# Creation Date: 11-05-2021
# Last Modified: Tue 11 May 2021 11:28:21 -03
# Agrupa números não negativos em uma lista e negativo em outra

def agrupa_negativos(lista):
    resultado = {'nao-negativos':[], 'negativos':[]}
    for numero in lista:
        if numero >= 0:
            resultado['nao-negativos'].append(numero)
        else:
            resultado['negativos'].append(numero)
    return resultado


#print(agrupa_negativos([10, -2, -7, 8])) 
assert agrupa_negativos([10, -2, -7, 8]) == {"nao-negativos":[10, 8], "negativos":[-2,-7]}
assert agrupa_negativos([-1, -5]) == {"nao-negativos":[ ], "negativos":[-1, -5]}
