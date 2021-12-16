# (py) amiltoncristian9@gmail.com
# Date: 30/03/2021, Last Change: Never
# Imprime a posição que cada time ocupa na tabela com ranking cumulativo

num_times = int(input())
lista_times = []
lista_pontos = []
lista_classificacao = []
contador = 1
time_atual = 0
time_seguinte = 1

for i in range(num_times):
    lista_times.append(input())
    lista_pontos.append(int(input()))

lista_pontos.append(-1)

for i in range(num_times):
    lista_classificacao.append(contador)
    contador += 1

for i in range(num_times):
    if lista_pontos[time_seguinte] == lista_pontos[time_atual]:
        lista_classificacao[time_seguinte] = lista_classificacao[time_atual]
    time_atual += 1
    time_seguinte += 1

for i in range(num_times):
    print(f'{lista_classificacao[i]}. {lista_times[i]} ({lista_pontos[i]})')
