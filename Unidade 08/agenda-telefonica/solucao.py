# (c) amiltoncristian9@gmail.com
# Creation Date: 24-04-2021
# Last Modified: sáb 24 abr 2021 21:59:28
# Agenda telefonica dinâmica

def inserir_contatos_na_agenda(agenda):
    entradas = int(input())
    for i in range(entradas):
        nome = input()
        telefone = input()
        agenda_telefonica.append([f'Nome: {nome}', f'Fone: {telefone}'])

# -------------------- ORGANIZAR A LISTA, FALTA TERMINARRRRRRR
def organizar_contatos_na_agenda(agenda):
    menor_nome = agenda.pop(0)
    while len(agenda) > 0:
        agenda_aux.append(agenda.pop(0))
    for contato in range(1, len(agenda_aux) -1):
        if (contato_aux[contato].split('Nome: '))[1] < menor_nome:
            menor_nome = 


def buscar_contatos_por_nome(agenda):
    nome_busca = input()
    contato_existe = False
    for contato in agenda:
        if (contato[0].split('Nome: '))[1] == nome_busca:
            saida.append(contato)
            contato_existe = True
    if not contato_existe:
        saida.append(['Nome inexistente'])


def imprimir_todos_contatos(agenda):
    for contato in agenda:
        saida.append(contato)


agenda_telefonica, saida = [], []
comando = 'esperando comando'

while True:
    comando = input()
    if comando == 'finalizar': break
    elif comando == 'inserir':
        inserir_contatos_na_agenda(agenda_telefonica)
        if len(agenda_telefonica) > 1:
            organizar_contatos_na_agenda(agenda_telefonica)
    elif comando == 'buscar':
        buscar_contatos_por_nome(agenda_telefonica)
    elif comando == 'imprimir':
        imprimir_todos_contatos(agenda_telefonica)

if len(saida) > 0:
    for contato in saida:
        for item in contato:
            print(item)
        print('----------')
