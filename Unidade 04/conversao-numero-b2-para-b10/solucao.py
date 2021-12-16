# (py) amiltoncristian9@gmail.com
# Creation Date: 07-04-2021
# Last Modified: qua 07 abr 2021 19:05:25
# Converter um número binário para decimal 

binario = input()
casa = 1
resultado = 0

for i in binario:
    multiplicador = 2 ** (len(binario) - (casa))
    casa += 1
    multiplicacao = int(i) * multiplicador
    resultado += multiplicacao
    print(f'{i} * {multiplicador} = {multiplicacao}')

print(f'{binario}(2) = {resultado}(10)')

