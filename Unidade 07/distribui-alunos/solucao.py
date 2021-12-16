# (py) amiltoncristian9@gmail.com
# Creation Date: 19-04-2021
# Last Modified: seg 19 abr 2021 17:47:48
# Distribuir de forma igualitária os alunos de duas turmas em dois labolatórios

def distribui_alunos(turma1, turma2, capacidade):
    lab1 = []
    lab2 = []
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


'''
t2 = [10]
t1 = [43, 23, 44, 213, 33, 75, 46,35,7,2,6,4,7]
print( distribui_alunos(t1, t2, 10) )'''
