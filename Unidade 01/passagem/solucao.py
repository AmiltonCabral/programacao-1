# Cartão de passagem aerea e calcula porcentagem do imposto
# 2020-03-12, amilton.cabral@ccc.ufcg.edu.br

identificador = input()
horario = input()
assento = input()
portao = input()
n_semtax = float(input())
n_comtax = float(input())

n_percent = (n_comtax - n_semtax) * 100 / n_comtax

print('### Cartão de Embarque ###')
print(f'Identificador do voo: {identificador}')
print(f'Horário: {horario}')
print(f'Assento: {assento}')
print(f'Portão: {portao}')
print(f'Total de Imposto: {n_percent:.1f}%')
