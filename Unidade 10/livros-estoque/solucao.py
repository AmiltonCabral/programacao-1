# (c) amiltoncristian9@gmail.com
# Creation Date: 11-05-2021
# Last Modified: Tue 11 May 2021 13:39:54 -03
# Conta quantos titulos zerados tem na biblioteca

def ausentes(estoque):
    titulos_zerados = 0
    for livro in estoque:
        if estoque[livro] == 0:
            titulos_zerados += 1
    return titulos_zerados


livros = { "Metamorfose": 30, "O Principe": 0, "Vigiar e Punir": 0, "Dumbo": 22}
livros1 = {}
livros2 = {'Torre negra': 0}
assert ausentes(livros) == 2
assert ausentes(livros1) == 0
assert ausentes(livros2) == 1
