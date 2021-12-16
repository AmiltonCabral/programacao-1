# (py) amiltoncristian9@gmail.com
# Creation Date: 14-04-2021
# Last Modified: qua 14 abr 2021 22:25:48
# Criar meu método join

def meu_join(delimitador, seq):
    result = ''
    for i in range(len(seq)):
        result += seq[i]
        if i == len(seq) -1: break
        result += delimitador
    return result
