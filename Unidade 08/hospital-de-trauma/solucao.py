# (c) amiltoncristian9@gmail.com
# Creation Date: 26-04-2021
# Last Modified: seg 26 abr 2021 21:41:31
# Organizar uma lista de espera de um hospital de acordo com a prioridade

def cadastra(fila, nome, prioridade): 
    if prioridade == 'vermelho':
        lista_espera[0].append(nome)
    elif prioridade == 'laranja':
        lista_espera[1].append(nome)
    elif prioridade == 'amarelo':
        lista_espera[2].append(nome)
    elif prioridade == 'verde':
        lista_espera[3].append(nome)
    elif prioridade == 'azul':
        lista_espera[4].append(nome)


def mostrar_pacientes(fila):
    for cor in fila:
        for paciente in cor:
            print(paciente)
    print('---')


def resumo(fila):
    paciente_cor = []
    for i in range(len(fila)):
        paciente_cor.append(len(fila[i]))
    return paciente_cor


def mostrar_resumo(fila):
    for i in range(len(fila)):
        if i == 0:
            print(f'vermelho: {paciente_classificado_cor[i]}')
        elif i == 1:
            print(f'laranja: {paciente_classificado_cor[i]}')
        elif i == 2:
            print(f'amarelo: {paciente_classificado_cor[i]}')
        elif i == 3:
            print(f'verde: {paciente_classificado_cor[i]}')
        elif i == 4:
            print(f'azul: {paciente_classificado_cor[i]}')
    print('---')


lista_espera = [[],[],[],[],[]]
while True:
    comando = input().split()
    if comando == ['fim']: break
    cadastra(lista_espera, comando[0], comando[1])

mostrar_pacientes(lista_espera)
paciente_classificado_cor = resumo(lista_espera)
mostrar_resumo(lista_espera)


'''print('------------------')
print(lista_espera)'''
