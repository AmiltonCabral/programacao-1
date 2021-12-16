# (py) amiltoncristian9@gmail.com
# Creation Date: 22-04-2021
# Last Modified: qui 22 abr 2021 08:40:41
# Distribuir de forma igualitária os alunos de duas turmas em dois labolatórios

def distribui_alunos(turma1, turma2, capacidade):
    lab1, lab2 = [], []
    passou = False
    while True:
        if len(lab1) < capacidade:
            if len(turma1) > 0:
                lab1.append(turma1.pop(0))
                passou = False
            if len(turma2) > 0 and len(lab1) < capacidade:
                lab1.append(turma2.pop(0))
                passou = True
        elif len(lab2) < capacidade:
            if len(turma1) > 0 and passou == True:
                lab2.append(turma1.pop(0))
            if len(turma2) > 0:
                lab2.append(turma2.pop(0))
                passou = True
        if len(turma2) < 1:
            passou = True
        if len(turma1) < 1 and len(turma2) < 1: break

    return [lab1, lab2]
