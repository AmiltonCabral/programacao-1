# (c) amiltoncristian9@gmail.com
# Creation Date: 11-05-2021
# Last Modified: Tue 11 May 2021 11:58:32 -03
# Mostrar quantos creditos tem um professor e quais disciplinas ele da aula

def disciplinas(alocacao, professor):
    saida_disciplina = []
    saida_creditos = 0
    for disciplina in alocacao:
        for professores in alocacao[disciplina]:
            if professores == professor:
                saida_disciplina.append(disciplina[0])
                saida_creditos += disciplina[1]
    saida = (saida_disciplina, saida_creditos)
    return saida


alocacao={("P1", 4): ['Jorge', 'Dalton','Wilkerson'],
          ("LP1", 4): ['Jorge', 'Dalton', 'Eliane', 'Wilkerson'],
          ("EVOL", 2): ['Dalton'],
          ("IC", 4): ['Eliane', 'Joseana'],
          ("P2", 4): ['Livia', 'Raquel', 'Nazareno'],
          ("GRAFOS", 2): ['Patricia', 'Patricia']}

assert set(disciplinas(alocacao, "Dalton")[0]) == set(['P1', 'LP1', 'EVOL'])
assert disciplinas(alocacao, "Dalton")[1] == 10
assert set(disciplinas(alocacao, "Eliane")[0]) == set(['LP1', 'IC'])
assert disciplinas(alocacao, "Eliane")[1] == 8
assert set(disciplinas(alocacao, "Patricia")[0]) == set(['GRAFOS'])
assert disciplinas(alocacao, "Patricia")[1] == 4
