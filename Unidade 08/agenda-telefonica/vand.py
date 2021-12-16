def ordem_alfabetica(lista):
    for elemento in lista:
        for i in range(len(lista)-1,-1,-1):
            if i == 0: break
            if lista[i] < lista[i-1]:
                lista[i], lista[i-1] = lista[i-1] , lista[i]
                numeros[i], numeros[i-1] = numeros[i-1] , numeros[i]

def inserir(n):
    for i in range(n):
        nome = input()
        numero = input()
        nomes.append(nome)
        numeros.append(numero)
    ordem_alfabetica(nomes)


def buscar(nome):
    validacao = False
    for i in range(len(nomes)):
        if nome == nomes[i]:
            validacao = True
            buscas.append(f'Nome: {nomes[i]}\nFone: {numeros[i]}\n----------')
    if validacao == False:
        buscas.append('Nome inexistente\n----------')

def imprimir():
    for intem in buscas:
        impressao.append(intem)
    for i in range(len(nomes)):
        impressao.append(f'Nome: {nomes[i]}\nFone: {numeros[i]}\n----------')

def finalizar():
    for item in impressao:
        print(item)

impressao = []
nomes = []
numeros = []
buscas = []

while True:
    operacao = input()
    if operacao == 'finalizar':
        finalizar()
        break
    if operacao == 'imprimir':
        imprimir()
    elif operacao == 'inserir':
        inserir(int(input()))
    elif operacao == 'buscar':
        buscar(input())
