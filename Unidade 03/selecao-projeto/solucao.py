# (py) amiltoncristian9@gmail.com
# Date: 24/03/2021, Last Change: Never
# Determinar a qual a situação do aluno para participar do projeto, de acordo com sua experiencia, CRE e nota da entrevista 

n_cre = float(input())
n_xp = int(input())
n_entrevista = float(input())

if n_cre < 7.0 and n_xp < 6:
    print(f'Candidato eliminado. CRE e experiência abaixo do limite.')

elif n_cre < 7.0:
    print(f'Candidato eliminado. CRE abaixo do limite.')

elif n_xp < 6:
    print(f'Candidato eliminado. Experiência abaixo do limite.')

elif n_entrevista <= 3:
    print(f'Candidato classificado.')

elif n_entrevista > 3:
    print(f'Candidato aprovado.')
