# (py) amiltoncristian9@gmail.com
# Creation Date: 09-04-2021
# Last Modified: sex 09 abr 2021 11:32:47
# Descobrir se uma chave tem 3 caracteres seguidos iguais, mais de 5 vogais ou é segura

chave = input()
chave += '00'
vogais = 0
parada = False

while True:
    for i in range(len(chave) -2):
        if chave[i] in 'aeiouAEIOU':
            vogais += 1
        if vogais > 5:
            out = 'vogais'
            break
        
        if chave[i] == chave[i +1] and chave[i] == chave[i +2]:
            out = 'consecutivos'
            break
        out = 'seguro'
    
    if out == 'vogais':
        print('Chave insegura. 6 vogais.')
    elif out == 'consecutivos':
        print('Chave insegura. 3 caracteres consecutivos iguais.')
    else:
        print('Chave segura!')
    break
