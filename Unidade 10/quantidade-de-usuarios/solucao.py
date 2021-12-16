# (c) amiltoncristian9@gmail.com
# Creation Date: 08-05-2021
# Last Modified: Sat 08 May 2021 14:46:42 -03
# Contar quantas pessoas tem a senha

def quantidade_usuarios(cadastro):
    quantidade_pessoas = 0
    for senha in cadastro:
        if senha != 9999:
            for usuario in cadastro[senha]:
                quantidade_pessoas += 1

    return quantidade_pessoas


lsd = {1234:['Andrey'], 1226:['Nazareno', 'Livia'], 9999:['administrador'] }
deq = {1114:['Ana'] }
assert quantidade_usuarios(lsd) == 3
assert quantidade_usuarios(deq) == 1
