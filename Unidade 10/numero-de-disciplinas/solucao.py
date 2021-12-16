# (c) amiltoncristian9@gmail.com
# Creation Date: 12-05-2021
# Last Modified: Wed 12 May 2021 15:52:52 -03
# Descobrir quantas disciplinas o aluno pode cursar
# Obs.:
# Nao pode duas disciplinas no mesmo horario
# Cursado disciplinas que sao pre-requisitos

def verifica_pre_requisito(grade, cursados, disciplina):
    # Descarta disciplinas cursadas
    for curso in cursados:
        if curso == disciplina:
            return False
    # Verifica se tem pre requisito
    if grade[disciplina] == []: return True
    for curso in grade[disciplina]:
        cursou = False
        for curso_feito in cursados:
            if curso == curso_feito:
                cursou = True
                break
        if not cursou: return cursou
    return True


def verifica_choque_horario(bd_horarios, disciplina, meus_horarios):
    novo_horario = bd_horarios[disciplina]
    for horario in meus_horarios:
        if horario == novo_horario:
            return False
    meus_horarios.append(novo_horario)
    return True


def numero_disciplinas(grade, horarios, cursados):
    meus_horarios = []
    possibilidades = 0
    for disciplina in grade:
        if not verifica_pre_requisito(grade, cursados, disciplina): continue
        if not verifica_choque_horario(horarios, disciplina, meus_horarios): continue
        possibilidades += 1
    return possibilidades


grade = {"p1": [], "lp1": [], "ic": [],"calc1": [], "p2": ["ic", "p1", "lp1"],
"lp2": ["ic", "p1", "lp1"], "grafos": ["ic", "p1", "lp1"], "calc2"  : ["calc1"],
"edados": ["ic", "p1", "lp1", "p2", "lp2", "grafos"],
"leda": ["ic", "p1", "lp1", "p2", "lp2", "grafos"]}

horarios= {"p1": "s082", "lp1": "x082", "ic": "i142", "calc1": "q082", "p2": "t162",
"lp2": "s082", "grafos": "q082", "calc2": "x162", "edados": "x162", "leda": "t102"}

assert numero_disciplinas(grade, horarios, ["ic", "p1", "lp1"]) == 3
assert numero_disciplinas(grade, horarios, []) == 4
