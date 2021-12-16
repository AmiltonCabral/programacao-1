# (py) amiltoncristian9@gmail.com
# Creation Date: 19-04-2021
# Last Modified: seg 19 abr 2021 09:49:33
# Comparar duas listas, se tiver 3 ou mais artistas iguais retorna verdadeiro

def tem_afinidade(lst1, lst2):
    afinidades = 0
    saida = False
    for artista_1 in lst1:
        for artista_2 in lst2:
            if artista_1 == artista_2:
                afinidades += 1
    if afinidades >= 3:
        saida = True

    return saida
