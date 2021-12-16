# (c) amiltoncristian9@gmail.com
# Creation Date: 11-05-2021
# Last Modified: Tue 11 May 2021 11:15:30 -03
# Inverte a chave com os valores em um dicionário

def meu_in(dic, valor):
    for elemento in dic:
        if elemento == valor:
            return True
    return False


def insercao_ordenada(dic, elemento):
    dic.append(elemento)
    for i in range(len(dic) -1, 0, -1):
        if dic[i] < dic[i-1]:
            dic[i], dic[i-1] = dic[i-1], dic[i]


def inverte_dicionario(dic):
    dic_inverso = {}
    for chave in dic:
        if meu_in(dic_inverso, dic[chave]):
            insercao_ordenada(dic_inverso[dic[chave]], chave)
        else:
            dic_inverso[dic[chave]] = [chave]
    
    return dic_inverso


m = {"a": 2, "b": 3, "c": 2}
n = {}
o = {'z':9}
p = {'a':3, 'c':9, 'e':4, 'g':10, 'i':1, 'k':9, 'm':3}
q = {'x':3, 'y':3}
d = {3: "a", 2: "a", 1: "a"}
#print(inverte_dicionario(q))
assert inverte_dicionario(m) == {2:["a","c"], 3:["b"]}
assert inverte_dicionario(n) == {}
assert inverte_dicionario(o) == {9: ['z']}
assert inverte_dicionario(p) == {3:['a','m'], 9:['c','k'], 4:['e'], 10:['g'], 1:['i']}
assert inverte_dicionario(q) == {3:['x','y']}
assert inverte_dicionario(d) == {"a": [1, 2, 3],}
