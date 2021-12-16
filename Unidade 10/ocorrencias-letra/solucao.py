# (c) amiltoncristian9@gmail.com
# Creation Date: 10-05-2021
# Last Modified: Mon 10 May 2021 18:13:16 -03
# Mostrar qual letra aparece mais e quantas vezes em uma frase

def adiciona_letra_dic(caractere):
    for letra in letras_texto:
        if letra == caractere:
            letras_texto[caractere] += 1
            return
    letras_texto[caractere] = 1


def detectar_maior_ocorrencia(letras_texto):
    maior = ('', 0)
    for letra in letras_texto:
        if letras_texto[letra] > maior[1]:
            maior = (letra, letras_texto[letra])
    return maior


texto = input().lower()
letras_texto = {}

for caractere in texto:
    if caractere != ' ':
        adiciona_letra_dic(caractere)

if len(letras_texto) > 0:
    maior_ocorrencia = detectar_maior_ocorrencia(letras_texto)
    print(f'{maior_ocorrencia[0]} {maior_ocorrencia[1]}')
