# Creation Date: 10-04-2021
# Last Modified: sáb 10 abr 2021 21:08:52

fundo, media, repeticoes = 0, 0, 0

while True:
    novo_valor = float(input())
    if novo_valor < media:
        print(f'Saldo total do FIS: R${fundo:.2f}.')
        print(f'Média das contribuições: R${media:.2f}.')
        break

    repeticoes += 1
    fundo += novo_valor
    media = fundo / repeticoes
