# (py) amiltoncristian9@gmail.com
# Date: 15/03/2001, Last Change: Never
# Calcular rendimento por hora de trabalho

n_salario_bruto = float(input())
n_horas_trabalhadas = int(input())

n_ganhos_hora = n_salario_bruto / n_horas_trabalhadas
n_desconto_ir = n_salario_bruto * (11 / 100)
n_desconto_inss = n_salario_bruto * (8 / 100)
n_desconto_sindicato = n_salario_bruto * (5 / 100)
n_salario_liquido = n_salario_bruto - (n_desconto_ir + n_desconto_inss + n_desconto_sindicato)
n_hora_liquida = n_salario_liquido / n_horas_trabalhadas

print(f'Salário Bruto = {n_salario_bruto:.2f}')
print(f'Hora Bruta = {n_ganhos_hora:.2f}')
print(f'Desconto IR = {n_desconto_ir:.2f}')
print(f'Desconto INSS = {n_desconto_inss:.2f}')
print(f'Desconto Sindicato = {n_desconto_sindicato:.2f}')
print(f'Salário Líquido = {n_salario_liquido:.2f}')
print(f'Hora Líquida = {n_hora_liquida:.2f}')
