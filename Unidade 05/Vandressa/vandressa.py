contador = 1
soma = 0
media = soma / contador
while True:
    valor = float(input())
    media = soma / contador
    print(valor, media) #TESTEEEE
    if media > valor : break
    soma += valor
    contador += 1
media = soma / (contador - 1)
print(f'Saldo total do FIS: R${soma:.2f}.')
print(f'Média das contribuições: R${media:.2f}.')
