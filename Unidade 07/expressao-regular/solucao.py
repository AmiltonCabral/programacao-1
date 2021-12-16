# (py) amiltoncristian9@gmail.com
# Creation Date: 19-04-2021
# Last Modified: sáb 24 abr 2021 14:28:19
# Criar frase no formato regra1*regra2

def is_substring_expr(str1,str2):
    resultado = True
    comeco_fim = str2.split('*')

    for i in range(len(comeco_fim[0])):
        if comeco_fim[0][i] != str1[i]:
            resultado = False

    for i in range(-1, - (len(comeco_fim[1]) +1), -1):
        if comeco_fim[1][i] != str1[i]:
            resultado = False

    return resultado
