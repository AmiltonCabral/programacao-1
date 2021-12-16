# (py) amiltoncristian9@gmail.com
# Date: 18/03/2021, Last Change: Never
# Calcular preço da peça de acordo com a quatidade de letras

nome = input('Nome? ')
n_valor = float(input('Valor da letra (R$)? '))

n_letras = len(nome)
n_preco_final = n_letras * n_valor

print(f'Preço final: R$ {n_preco_final:.2f}')
