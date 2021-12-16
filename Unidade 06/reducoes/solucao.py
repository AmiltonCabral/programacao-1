# (py) amiltoncristian9@gmail.com
# Creation Date: 12-04-2021
# Last Modified: seg 12 abr 2021 22:31:13
# Criar uma função que retorna uma lista com as diferenças entre dois valores consecutivos

def reducoes(seq):
    reducao = []
    for i in range(len(seq) -1):
        subtracao = seq[i] - seq[i+1]
        if subtracao < 0:
            reducao.append(0)
        else:
            reducao.append(subtracao)
    return reducao
