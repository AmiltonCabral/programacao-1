# (c) amiltoncristian9@gmail.com
# Creation Date: 24-04-2021
# Last Modified: dom 25 abr 2021 17:51:15
# Agenda telefonica dinâmica

def inserir_contatos_na_agenda(agenda):
    entradas = int(input())
    for i in range(entradas):
        nome = input()
        telefone = input()
        agenda_telefonica.append([nome, telefone])


def organizar_contatos_na_agenda(agenda):
    trocou_valores = True
    while trocou_valores:
        trocou_valores = False
        for i in range(len(agenda) -1):
            if agenda[i][0] > agenda[i+1][0]:
                agenda[i], agenda[i+1] = agenda[i+1], agenda[i] 
                trocou_valores = True
                break


def buscar_contatos_por_nome(agenda):
    nome_busca = input()
    contato_existe = False
    for contato in agenda:
        if contato[0] == nome_busca:
            saida.append([f'Nome: {contato[0]}', f'Fone: {contato[1]}'])
            contato_existe = True
    if not contato_existe:
        saida.append(['Nome inexistente'])


def imprimir_todos_contatos(agenda):
    for contato in agenda:
        saida.append([f'Nome: {contato[0]}', f'Fone: {contato[1]}'])


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
