# (c) amiltoncristian9@gmail.com
# Creation Date: 11-05-2021
# Last Modified: Tue 11 May 2021 09:15:40 -03
# Descobrir quantos créditos um aluno tem de acordo com o bd

def num_creditos(bd_ufcg, matricula):
    creditos = 0
    for unidade_academica in bd_ufcg:
        for disciplina in bd_ufcg[unidade_academica]:
            for matricula_no_bd in bd_ufcg[unidade_academica][disciplina]:
                if matricula_no_bd == matricula:
                    creditos += disciplina[1]
    return creditos


bd_ufcg = {"UASC": {("Programação I", 4): ["11624100", "11624400"], ("Programação II", 4): ["11624200"], ("Teoria dos Grafos", 2): ["11624200"]},
           "UAF": {("Física Clássica", 4): ["11624200"], ("Física Moderna", 4): ["11624300", "11624500", "11624600"]},
           "UAM": {("Cálculo I", 4): ["11624100", "11624300"], ("Álgebra Linear", 4): ["11624300"]}
           }
bd_ufcg1 = {"UASC": {("Programação I", 4): ["11624100", "11624400"], ("Programação II", 4): ["11624200"], ("Teoria dos Grafos", 2): ["11624200"]}}
bd_ufcg2 = {}
assert num_creditos(bd_ufcg, "11624199") == 0
assert num_creditos(bd_ufcg1, "11624200") == 6
assert num_creditos(bd_ufcg2, "11624200") == 0
