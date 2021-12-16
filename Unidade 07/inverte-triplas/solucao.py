# (c) amiltoncristian9@gmail.com
# Creation Date: 21-04-2021
# Last Modified: qua 21 abr 2021 16:52:45
# Inverter indices de uma string por seu negativo de 3 em 3

def inverte3a3(s):
    lista_s, s_aux, itens_lista, s_saida = [], '', 0, ''
    for i, letra in enumerate(s):
        s_aux += letra
        if (i + 1) % 3 == 0:
            lista_s.append(s_aux)
            s_aux = ''
            itens_lista += 1

    for i in range(len(lista_s) // 2):
        neg_i = -(i + 1)
        lista_s[i], lista_s[neg_i] = lista_s[neg_i], lista_s[i]
    
    for i in lista_s:
        s_saida += i

    return s_saida


'''print(inverte3a3("abcdefAAAghijkl"))
print(inverte3a3("abcdef"))
print(inverte3a3("abcdefghijkl"))'''
