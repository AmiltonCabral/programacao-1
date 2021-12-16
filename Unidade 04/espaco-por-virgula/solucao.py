# (py) amiltoncristian9@gmail.com
# Date: 05/04/2021, Last Change: Never
# Substituir espaços por vírgula e pegar apenas os caracteres nos limites estabelecidos

frase = list(input())
inicio = int(input())
fim = int(input())
nova_frase = ''

for i in range(inicio, fim):
    if frase[i] == ' ':
        nova_frase += ','
    else:
        nova_frase += frase[i]
    if i == fim -1:
        break
    nova_frase += ' '

print(nova_frase)
