# (py) amiltoncristian9@gmail.com
# Date: 15/03/2021, Last Change: Never
# Calcula IMC e indica quanto deve ganhar ou perder de peso

n_peso = float(input())
n_altura = float(input())

n_imc = n_peso / n_altura ** 2
n_peso_ideal = 24.9 * n_altura ** 2
n_peso_recomendado = n_peso_ideal - n_peso

print(f'IMC atual = {n_imc:.2f}')
print(f'Peso a ser ganho/perdido = {n_peso_recomendado:.2f}')
