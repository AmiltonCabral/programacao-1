# (py) amiltoncristian9@gmail.com
# Date: 26/03/2021, Last Change: Never
# Descobrir quem é mais velho entre duas pessoas

nome_a = input()
dia_a = int(input())
mes_a = int(input())
ano_a = int(input())

nome_b = input()
dia_b = int(input())
mes_b = int(input())
ano_b = int(input())

mais_velho = 'nenhuma'

if ano_a < ano_b:
    mais_velho = nome_a

elif ano_a > ano_b:
    mais_velho = nome_b

elif mes_a < mes_b:
    mais_velho = nome_a

elif mes_a > mes_b:
    mais_velho = nome_b

elif dia_a < dia_b:
    mais_velho = nome_a

elif dia_a > dia_b:
    mais_velho = nome_b

print(mais_velho)
