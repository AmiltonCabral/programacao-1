# (py) amiltoncristian9@gmail.com
# Creation Date: 19-04-2021
# Last Modified: ter 20 abr 2021 08:57:37
# Descobrir elementos diferentes entre duas listas

def acordes(musica_1, musica_2):
    msc = []

    for i in musica_1:
        msc.append(i)

    for msc_two in musica_2:
        repetida = False
        for msc_one in msc:
            if msc_one == msc_two:
                repetida = True
        if repetida == False:
            msc.append(msc_two)
    
    return msc
