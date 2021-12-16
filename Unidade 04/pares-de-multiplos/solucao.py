# (py) amiltoncristian9@gmail.com
# Date: 06/04/2021, Last Change: Never
# Verificar se um número é par do seu vizinho

sequencia = input()
FATOR = int(input())

eh_par = 0

lista_sequencia = sequencia.split()
for i in range(len(lista_sequencia) -1):
    if int(lista_sequencia[i]) / int(lista_sequencia[i +1]) == FATOR:
        eh_par += 1
    elif int(lista_sequencia[i +1]) / int(lista_sequencia[i]) == FATOR:
        eh_par += 1

print(f'{eh_par} par(es)')

for i in range(len(lista_sequencia) -1):
    if int(lista_sequencia[i]) / int(lista_sequencia[i +1]) == FATOR:
        print(int(lista_sequencia[i]), int(lista_sequencia[i +1]))
    elif int(lista_sequencia[i +1]) / int(lista_sequencia[i]) == FATOR:
        print(int(lista_sequencia[i]), int(lista_sequencia[i +1]))       
