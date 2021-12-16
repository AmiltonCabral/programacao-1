# (py) amiltoncristian9@gmail.com
# Creation Date: 10-04-2021
# Last Modified: sáb 10 abr 2021 22:22:51
# Descobrir se o valor em BCD é válido

resultados = []
while True:
    valor = input()

    if valor == 'fim':
        break

    if len(valor) != 8:
        resultados.append('Tente novamente.')
    else:
        bcd = ''
        numero = ''
        numero += valor[0] + valor[1] + valor[2] + valor[3]
        bcd += str(int(numero, 2))
        numero = ''
        numero += valor[4] + valor[5] + valor[6] + valor[7]
        bcd += str(int(numero, 2))
    
        if len(bcd) > 2:
            resultados.append('BCD inválido.')
        else:
            resultados.append(bcd)

for i in resultados:
    print(i)
