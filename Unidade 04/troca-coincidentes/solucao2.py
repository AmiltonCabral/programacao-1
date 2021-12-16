# (py) amiltoncristian9@gmail.com
# Creation Date: 06-04-2021
# Last Modified: qui 08 abr 2021 08:28:50
# Decodificar palavra 

frase = list(input())
chave = input()
decodificado = list(frase)
saida = ''

for i in range(len(chave)):
    if str(i) == frase[i]:
        decodificado[i] = chave[i]

for i in decodificado:
    saida += i

print(saida)
