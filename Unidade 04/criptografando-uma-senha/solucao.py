# (py) amiltoncristian9@gmail.com
# Date: 03/04/2021, Last Change: Never
# A partir do segundo elemento de uma senha, converte algumas letras em números

contador = 0

palavra = input()
senha = list(palavra)
n_trocas = 0
str_senha = ''

for i in palavra:
    if i == 'a' or i == 'A':
        senha[contador] = '4'
        n_trocas += 1
    elif i == 'e' or i == 'E':
        senha[contador] = '3'
        n_trocas += 1
    elif i == 'i' or i == 'I':
        senha[contador] = '1'
        n_trocas += 1
    elif i == 'o' or i == 'O':
        senha[contador] = '0'
        n_trocas += 1
    contador += 1
    
if palavra[0] != senha[0]:
    n_trocas -= 1
    senha[0] = palavra[0]

for i in senha:
    str_senha += i

print(f'{str_senha} ({n_trocas} troca(s))')
