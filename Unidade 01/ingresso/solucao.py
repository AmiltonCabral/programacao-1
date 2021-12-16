# (py) amiltoncristian9@gmail.com
# Date: 10/03/2021, Last Change: 12/03/2021
# Valor total dos ingressos

n_adultos = int(input())
n_criancas = int(input())
n_preco = float(input())

total = (n_criancas * (n_preco / 2)) + n_adultos * n_preco

print(f"Total: R$ {total:.2f}")
