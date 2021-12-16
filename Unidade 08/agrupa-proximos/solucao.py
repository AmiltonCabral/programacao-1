# (c) amiltoncristian9@gmail.com
# Creation Date: 28-04-2021
# Last Modified: qua 28 abr 2021 19:11:32
# Descobre valores próximos

def agrupa_proximos(lista, valor, criterio):
    valores_proximos = []
    for i in lista:
        if 0 < i - valor < criterio or 0 < -1 * (i - valor) < criterio or i == valor:
            valores_proximos.append(i)
    return valores_proximos


l = [1,2,3,4,8,22,3,5]
print(agrupa_proximos(l,4,2))
print(l)
