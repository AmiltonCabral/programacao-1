# (py) amiltoncristian9@gmail.com
# Creation Date: 09-04-2021
# Last Modified: sáb 10 abr 2021 20:34:02
# Descobrir quantos alunos foram reprovados por falta

reprovados = 0

while True:
    presenca = input().lower()

    if presenca == '-':
        print(f'{reprovados} aluno(s) reprovado(s) por falta.')
        break

    faltas = 0        
    contador = 0
    while contador < len(presenca):
        if presenca[contador] == 'f':
            faltas += 1
        contador += 1

    if faltas > 8:
        reprovados += 1
