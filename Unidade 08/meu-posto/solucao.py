# (c) amiltoncristian9@gmail.com
# Creation Date: 24-04-2021
# Last Modified: sáb 24 abr 2021 16:52:00
# Programa que organiza um sistema de pontuação para clientes de uma rede de postos de combustivel

def cadastrar_novo_usuario(lista):
    cpf = input()
    nome = input()
    posto = input()
    if len(lista) > 0:
        for usuario in lista:
            if usuario[0] == cpf:
                return 'Usuário já existente.'
    pontos = 300
    lista.append([cpf, nome, posto, pontos])
    return 'Usuário cadastrado com sucesso.'


def atualizar_pontos(lista):
    cpf = input()
    posto = input()
    status = 'Usuário inexistente.'
    if len(lista) < 1:
        status = 'Usuário inexistente.'
    else:
        for usuario in lista:
            if usuario[0] == cpf:
                if usuario[2] == posto:
                    usuario[3] += 200
                else:
                    usuario[3] += 100
                status = 'Usuário atualizado com sucesso.'
    return status


def consultar_pontos(lista):
    cpf = input()
    if len(lista) < 1:
        status_sessao.append('Usuário inexistente.')
    else:
        usuario_existe = False
        for usuario in lista:
            if usuario[0] == cpf:
                usuario_existe = True
                status_sessao.append(f'Nome: {usuario[1]}')
                status_sessao.append(f'CPF: {usuario[0]}')
                status_sessao.append(f'Saldo: {usuario[3]:.2f}')
        if not usuario_existe:
            status_sessao.append('Usuário inexistente.')


comando = '-1'
lista_usuarios, status_sessao = [], []
while comando != 'finalizar':
    comando = input()
    if comando == 'cadastrar':
        status_sessao.append(cadastrar_novo_usuario(lista_usuarios))
    elif comando == 'atualizar':
        status_sessao.append(atualizar_pontos(lista_usuarios))
    elif comando == 'consultar':
        consultar_pontos(lista_usuarios)

for i in status_sessao:
    print(i)

'''print('----')
print(lista_usuarios)'''
