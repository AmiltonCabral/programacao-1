# (c) amiltoncristian9@gmail.com
# Creation Date: 24-04-2021
# Last Modified: sáb 24 abr 2021 20:05:33
# Retornar os alunos da turma N

def cria_lista_presenca(lista_turmas, nomes, num_turma):
    alunos = []
    for i, turma in enumerate(lista_turmas):
        if turma == num_turma:
            alunos.append(nomes[i])
    return alunos


'''turmas = [1, 2, 2, 4, 5, 3, 5]
nomes = ["Maria", "Pedro", "Carlos", "Ana", "Carla", "Joao", "Jose"]
print(cria_lista_presenca(turmas, nomes, 5))'''
