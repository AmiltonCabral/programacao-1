# (c) amiltoncristian9@gmail.com
# Creation Date: 30-04-2021
# Last Modified: sex 30 abr 2021 16:49:35
# Remove alunos inaptos a fazer uma prova, seja por média insuficiente ou não estar inscrito

def filtra_alunos(alunos, inscritos, media_min):
    removidos = 0
    for i in range(len(alunos) -1, -1, -1):
        remove = True
        for inscrito in inscritos:
            if alunos[i][0] == inscrito:
                remove = False
                break
        if alunos[i][1] < media_min:
            remove = True
        if remove:
            alunos.pop(i)
            removidos += 1
    return removidos


'''inscritos = [121, 123, 124]
alunos = [ (120,8.0), (121,7.5), (122,5.0), (123,6.0), (124,9.0), (125,4.0) ]
print(filtra_alunos(alunos, inscritos, 7.0))
print(alunos)'''
