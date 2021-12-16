# (c) amiltoncristian9@gmail.com
# Creation Date: 11-05-2021
# Last Modified: Tue 11 May 2021 14:04:04 -03
# Descobrir quais os alunos pertecem as salas dos professores

def colegas_de_sala(salas, professor):
    num_sala = -1
    alunos_sala = []
    for pessoa in salas:
        if pessoa == professor:
            num_sala = salas[pessoa]
            break
    for aluno in salas:
        if salas[aluno] == num_sala and aluno != professor:
            alunos_sala.append(aluno)

    return alunos_sala


salasprofs = {
'Franklin': 206,    'Tiago':206,        'Eliane': 206,
'Adalberto':209,    'Wilkerson':207,    'Dalton': 204,
'Jorge': 204 }
assert set(colegas_de_sala(salasprofs, 'Franklin')) == set(['Tiago', 'Eliane'])
assert set(colegas_de_sala(salasprofs, 'Adalberto')) == set([])
