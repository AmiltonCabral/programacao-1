# (py) amiltoncristian9@gmail.com
# Date: 30/03/2021, Last Change: Never
# Identificar a que ponto os dados lidos são inconsistentes e contar quantos dados são validos

n_entradas = int(input())

lista_dados = []
contador = 0
num_negativo = 0

for i in range(n_entradas):
    entrada = input()
    lista_entrada = entrada.split()
    lista_dados += lista_entrada
    contador += 1
    num_negativo += 3
    if int(lista_entrada[0]) < 0:
        print('dado inconsistente. peso negativo.')
        num_negativo -= 3
        break
    elif int(lista_entrada[1]) < 0:
        print('dado inconsistente. combustível negativo.')
        num_negativo -= 2
        break
    elif int(lista_entrada[2]) < 0:
        print('dado inconsistente. altitude negativa.')
        num_negativo -= 1
        break

for i in range(n_entradas - contador):
    input()

print(f'{num_negativo} dados válidos.')
