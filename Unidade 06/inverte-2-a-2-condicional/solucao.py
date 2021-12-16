# (py) amiltoncristian19@gmail.com
# Creation Date: 13-04-2021
# Last Modified: ter 13 abr 2021 20:45:54
# Inverte valores se um for menor que o outro e pula 2 casas

def inverte2a2_condicional(seq):
    new_seq = seq
    palavra = ''
    for i in range(0, len(seq)-1, 2):
        num = seq[i]
        if seq[i] > seq[i+1]:
            new_seq[i] = seq[i+1]
            new_seq[i+1] = num

    return new_seq
