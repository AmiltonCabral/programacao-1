# (py) amiltoncristian9@gmail.com
# Date: 30/03/2021, Last Change: Never
# Recebe duas listas com receitas e despesas e calcula lucro

mes_count = 0
meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']

for i in range(12):
    entrada = input()
    valores = entrada.split()
    receita = float(valores[0])
    despesa = float(valores[1])
    lucro = receita - despesa
    mes_atual = meses[mes_count]
    mes_count += 1
    if lucro < 0:
        espacos = ' '
    else:
        espacos = '  '
    print(f'{mes_atual}{espacos}{lucro:.1f}')
