def calcula_digitos_verificacao(numeros):
    digitos = ''
    while len(digitos) != 2:
        multiplicador = 1
        somacalculo = 0
        for i in range(len(numeros)):
            indice = 0 - (i + 1)
            elemento = numeros[indice]
            multiplicador += 1
            calculo = int(elemento) * multiplicador
            somacalculo += calculo
        digito = (somacalculo * 10) % 11

        if digito == 10: digitos += '0'
        else: digitos += f'{digito}'

        numeros += f'{digito}'
    return digitos
print( calcula_digitos_verificacao('983948') )

#print( calcula_digitos_verificacao('12389461237542394877912364892317487123894781237492361489623178412374878923164792361479') )
