# (py) amiltoncristian9@gmail.com
# Date: 22/03/2021, Last Change: 25/03/2021
# O programa ler dados e detecta qual nota cada aluno obteve, depois diz qual aluno teve a melhor nota

n_quant_alunos = int(input())
n_nota = 0
n_todas_notas = []
contador = 0
n_aluno = 0
n_maior_nota = 0

# Cria uma lista com todas as notas
for _ in range(n_quant_alunos):
    n_resultado = input()
    for ponto in n_resultado:
        if ponto == ".":
            n_nota += 1
    n_todas_notas.append(n_nota)
    n_nota = 0

# Escolhe a melhor nota da lista
for _ in range(len(n_todas_notas)):
    n_nota = n_todas_notas[contador]
    contador += 1
    if n_maior_nota < n_nota:
        n_maior_nota = n_nota

# Diz a posição da melhor nota na lista
if n_maior_nota == 0:
    print(-1)
else:
    for i in n_todas_notas:
        n_aluno += 1
        if i == n_maior_nota:
            print(n_aluno)
            break
