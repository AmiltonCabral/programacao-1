# (py) amiltoncristian9@gmail.com
# Creation Date: 14-04-2021
# Last Modified: dom 18 abr 2021 21:07:13
# Criar digito verificador

def calcula_digitos_verificacao(cpf): 
    lista_cpf = list(cpf)
    resto = ''
    for i in range(2):
        multiplicado = 0
        for i in range(len(lista_cpf)):
            ultimo_digito = lista_cpf.pop()
            multiplicado += int(ultimo_digito) * (i+2)
        resto += str(((multiplicado * 10) % 11) % 10)
        lista_cpf = list(cpf)
        lista_cpf.append(resto)
    return resto

print( calcula_digitos_verificacao('983948') )
