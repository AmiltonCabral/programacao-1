# (py) amiltoncristian9@gmail.com
# Date: 25/03/2021, Last Change: Never
# calcular media dos alunos 

n_mtp_feitas = int(input())

if n_mtp_feitas == 1:
    n1 = float(input())
    media = (n1)
    resultado = 'Aluno ainda não aprovado na unidade'

elif n_mtp_feitas == 2:
    n1 = float(input())
    n2 = float(input())
    media = (n1 + n2) / 2
    if media < 6.0:
        resultado = 'Aluno ainda não aprovado na unidade'
    else:
        resultado = 'Aluno aprovado na unidade'

elif n_mtp_feitas > 2:
    n1 = float(input())
    n2 = float(input())
    n3 = float(input())
    media = ((n1 + n2 + n3) / 3) - 0.5
    if media < 6.0:
        resultado = 'Aluno ainda não aprovado na unidade'
    else:
        resultado = 'Aluno aprovado na unidade'

print(media)
print(resultado)
