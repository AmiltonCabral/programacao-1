# (c) amiltoncristian9@gmail.com
# Creation Date: 20-05-2021
# Last Modified: Thu 20 May 2021 09:21:48 -03
# 

def senha(cadastro, usuario):
    for senhas in cadastro:
        for pessoas in cadastro[senhas]:
            if pessoas == usuario:
                return senhas
    return -1


splab = {1313:['Franklin', 'Jorge'], 1226:['Eliane', 'Dalton'], 1507:['Wilkerson'] }
assert senha(splab, 'Matheus') == -1
assert senha(splab, 'Franklin') == 1313
