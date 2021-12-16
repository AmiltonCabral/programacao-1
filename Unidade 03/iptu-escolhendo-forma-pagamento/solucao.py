# (py) amiltoncristian9@gmail.com
# Date: 23/03/2021, Last Change: Never
# Programa recebe área da casa, valor do m² e forma de pagamento, entregando ao usuário o valor do imposto

n_area_casa = float(input())
n_valor_regiao = float(input())
opcao_pagamento = input()
n_valor_inteiro = n_area_casa * n_valor_regiao
n_preco = 0


if opcao_pagamento == 'vista':
    n_preco = n_valor_inteiro * 80 / 100
    print(f'Total: R$ {n_preco:.2f}')

elif opcao_pagamento == '2x':
    n_preco = n_valor_inteiro * 90 / 100
    n_parcelas = n_preco / 2
    print(f'Total: R$ {n_preco:.2f}.', end=' ')
    print(f'Parcelas: R$ {n_parcelas:.2f}')

elif opcao_pagamento == '3x':
    n_preco = n_valor_inteiro * 95 / 100
    n_parcelas = n_preco / 3
    print(f'Total: R$ {n_preco:.2f}.', end=' ')
    print(f'Parcelas: R$ {n_parcelas:.2f}')
