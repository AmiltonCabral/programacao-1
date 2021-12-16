# (py) amiltoncristian9@gmail.com
# Date: 24/03/2021, Last Change: Never
# Decide se a pessoa paga meia entrada, é isento ou inteiro de acordo com a idade

n_idade = int(input('Idade? '))

eh_estudante = ''
eh_rede_publica = ''

if n_idade < 12:
    print('criança (meia entrada)')
elif n_idade >= 65:
    print('idoso (meia entrada)')
else:
    eh_estudante = input('Estudante? ')

    if eh_estudante == 'n':
        print('adulto (inteira)')
    else:
        eh_rede_publica = input('Rede Pública? ')

    if eh_rede_publica == 's':
        print('estudante da rede pública (isento)')
    elif eh_rede_publica == 'n':
        print('estudante (meia entrada)')
