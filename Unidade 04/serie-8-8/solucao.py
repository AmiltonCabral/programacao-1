# (py) amiltoncristian9@gmail.com
# Date: 31/03/2021, Last Change: Never
# Imprimir uma sequência que pula de 0.2 em 0.2

contador = 8.8

for i in range(100**2):
    print(f'{contador:.1f}')
    if contador > 100.0:
        break
    contador += 0.2
