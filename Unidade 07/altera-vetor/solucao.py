# (py) amiltoncristian9@gmail.com
# Creation Date: 20-04-2021
# Last Modified: ter 20 abr 2021 09:44:03
# Multiplica um vetor por um escalar e deixa negativo

def altera_vetor_por_escalar(vetor, escalar):
    for i in range(len(vetor)):
        vetor[i] = vetor[i] * escalar
