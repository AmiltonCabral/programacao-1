# (py) amiltoncristian9@gmail.com
# Date: 18/03/2021, Last Change: Never
# Calcular preço para trocar moldura

n_comprimento = float(input())
n_largura = float(input())

n_comprimento_m = n_comprimento / 100
n_largura_m = n_largura / 100
n_preco = (n_comprimento_m * 120 + n_largura_m * 120) * 2

print(f'R$ {n_preco:.1f}')
