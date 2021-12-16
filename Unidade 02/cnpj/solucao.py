# (py) amiltoncristian9@gmail.com
# Date: 17/03/2021, Last Change: Never
# Formar o dígito verificador do CNPJ

raiz_cnpj = input()

n_soma_raiz = sum(int(x) for x in raiz_cnpj if x.isdigit())
n_digito_verificador = n_soma_raiz + 1

print(f'{raiz_cnpj}/0001-{n_digito_verificador:02d}')
