# (py) amiltoncristian9@gmail.com
# Date: 31/03/2021, Last Change: Never
# Compara quantas letras são semelhantes de uma palavra com sua inversa

palavra = input()
contador = len(palavra) - 1
resultado = 0

for i in palavra:
    if palavra[contador] == i:
        resultado += 1
    contador -= 1

print(f'A palavra {palavra} contém {resultado} caractere(s) coincidente(s) com a sua inversa.')
