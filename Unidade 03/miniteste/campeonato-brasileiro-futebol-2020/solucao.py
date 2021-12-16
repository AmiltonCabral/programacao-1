# (py) amiltoncristian9@gmail.com
# Date: 26/03/2021, Last Change: Never
# Dentre dois times de futebol, descobrir quem foi campeão na classificação

n_a_pontos = int(input())
n_a_vitorias = int(input())
n_a_gols_pro = int(input())
n_a_gols_contra = int(input())
n_b_pontos = int(input())
n_b_vitorias = int(input())
n_b_gols_pro = int(input())
n_b_gols_contra = int(input())

n_a_saldo_gols = n_a_gols_pro - n_a_gols_contra
n_b_saldo_gols = n_b_gols_pro - n_b_gols_contra

if n_a_pontos > n_b_pontos:
    vencedor = 'A'
    perdedor = 'B'

elif n_a_pontos < n_b_pontos:
    vencedor = 'B'
    perdedor = 'A'

elif n_a_vitorias > n_b_vitorias:
    vencedor = 'A'
    perdedor = 'B'

elif n_a_vitorias < n_b_vitorias:
    vencedor = 'B'
    perdedor = 'A'

elif n_a_saldo_gols > n_b_saldo_gols:
    vencedor = 'A'
    perdedor = 'B'

elif n_a_saldo_gols < n_b_saldo_gols:
    vencedor = 'B'
    perdedor = 'A'

else:
    vencedor = 'empate'
    perdedor = 'empate'

if vencedor == 'A':
    print(f'O Time A ganhou do Time B.')

elif vencedor == 'B':
    print(f'O Time B ganhou do Time A.')

else:
    print('Os dois times terminaram empatados.')
