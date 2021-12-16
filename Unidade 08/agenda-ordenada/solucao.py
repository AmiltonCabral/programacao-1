# (c) amiltoncristian9@gmail.com
# Creation Date: 22-04-2021
# Last Modified: qui 22 abr 2021 18:37:25
# Criar uma agenda que atualiza a cada entrada mantendo ordem alfabetica

def organizar_lista(d_agenda, d_nome):
    agenda_aux = []
    nome_entrou = False
    contador = -1
    if len(d_agenda) == 0:
        d_agenda.append(d_nome)
        return 0
    while len(d_agenda) > 0:
        agenda_aux.append(d_agenda.pop())
    while len(agenda_aux) > 0 or not nome_entrou:
        contador += 1
        if len(agenda_aux) > 0 and nome < agenda_aux[-1] and not nome_entrou:
            d_agenda.append(nome)
            nome_entrou = True
            last_name = contador
        elif len(agenda_aux) > 0:
            d_agenda.append(agenda_aux.pop())
        elif not nome_entrou:
            d_agenda.append(nome)
            nome_entrou = True
            last_name = contador
    return last_name


agenda = []
while True:
    nome = input()
    if nome == '####': break

    last_name = organizar_lista(agenda, nome)

    for i, item in enumerate(agenda):
        if i == last_name:
            print(f'* {item}')
        else:
            print(item)
    print('----')
