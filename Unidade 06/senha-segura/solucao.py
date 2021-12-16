# (py) amiltoncristian9@gmail.com
# Creation Date: 14-04-2021
# Last Modified: qua 14 abr 2021 15:55:31
# Descobre se uma senha é segura

def senha_segura(senha):
    eh_segura = 'Senha segura'
    if len(senha) < 4:
        eh_segura = 'Senha insegura'
    for i in range(0, len(senha), 2):
        if int(senha[i]) % 2 == 0:
            eh_segura = 'Senha insegura'
    for i in range(1, len(senha), 2):
        if int(senha[i]) % 2 == 1:
            eh_segura = 'Senha insegura'
    return eh_segura
