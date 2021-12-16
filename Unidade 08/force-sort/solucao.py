# (c) amiltoncristian9@gmail.com
# Creation Date: 27-04-2021
# Last Modified: ter 27 abr 2021 14:15:33
# Manter a lista em ordem crescente alterando o valor errado para o de indece anterior

def force_sort(seq):
    if len(seq) > 0:
        resultado = [0]
    else:
        resultado = []
    for i in range(1, len(seq)):
        if seq[i] < seq[i-1]:
            resultado.append(seq[i-1] - seq[i])
            seq[i] = seq[i-1]
        else:
            resultado.append(0)
    return resultado


'''#seq = [1, 3, 5, 4, 9]
#seq = [1, 3, 5, 4, 9, 2, 15]
seq = [2,1]
print(force_sort(seq))
print(seq)'''
