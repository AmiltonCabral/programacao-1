# (c) amiltoncristian9@gmail.com
# Creation Date: 29-04-2021
# Last Modified: qui 29 abr 2021 09:24:29
# Descobrir os unicos em comum em duas listas

def unicos_em_comum(seq1, seq2):
    comuns_seq1 = []
    for i in seq1:
        comum = 0
        for j in seq1:
            if i == j:
                comum += 1
        if comum == 1:
            comuns_seq1.append(i)
    comuns_seq2 = []
    for i in seq2:
        comum = 0
        for j in seq2:
            if i == j:
                comum += 1
        if comum == 1:
            comuns_seq2.append(i)
    resultado = []
    for i in comuns_seq1:
        for j in comuns_seq2:
            if i == j:
                resultado.append(i)
    return resultado



#seq1 = [ 'A', 'A', 'B', 'C', 'C', 'D']
#seq2 = ['B', 'A', 'C', 'D', 'D']
seq1 = ['A', 'B', 'A', 'B']
seq2 = ['C', 'C']
print(unicos_em_comum(seq1, seq2))
