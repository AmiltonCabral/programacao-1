# (py) amiltoncristian9@gmail.com
# Date: 12/03/2001, Last Change: Never
# Calcula tijolos e paredes para entregar orçamento

n_preco_tijolos = float(input('Digite o preço da unidade do tijolo (Em reais): '))
n_altura_tijolos = float(input('Digite a altura do tijolo (Em metros): '))
n_largura_tijolos = float(input('Digite o comprimento do tijolo (Em metros): '))
n_altura_parede = float(input('Digite a altura das paredes (Em metros): '))
n_largura_parede = float(input('Digite o comprimento das paredes (Em metros): '))


n_altura_necessaria = n_altura_parede / n_altura_tijolos
n_largura_necessaria = n_largura_parede / n_largura_tijolos
n_tijolos_total = n_altura_necessaria * n_largura_necessaria
n_orcamento = n_tijolos_total * n_preco_tijolos

print(f'O número total de tijolos é {n_tijolos_total:.1f} e o orçamento final é de R$ {n_orcamento:.1f}')
