# (c) amiltoncristian9@gmail.com
# Creation Date: 11-05-2021
# Last Modified: Tue 11 May 2021 13:47:58 -03
# Inverter um dicionario

def troca_chave(dic):
    novo_dic = {}
    for chave in dic:
        novo_dic[dic[chave]] = chave

    return novo_dic


assert troca_chave({1:2}) == {2:1}
assert troca_chave({1:2, 2:3, 3:4}) == {2:1, 3:2, 4:3}
assert troca_chave({ '@':'V','a':'v', 'n':'o'}) == { 'V':'@','v':'a', 'o':'n'}
