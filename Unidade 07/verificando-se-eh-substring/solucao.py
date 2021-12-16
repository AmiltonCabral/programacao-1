# (py) amiltoncristian9@gmail.com
# Creation Date: 15-04-2021
# Last Modified: qui 15 abr 2021 15:52:53
# Verificar se tem uma string dentro de outra

def is_substring(str1, str2): 
    resultado = False
    for i in range(len(str1)):
        if str1[i: len(str2) +i] == str2:
            resultado = True
    return resultado
