# (py) amiltoncristian9@gmail.com
# Date: 23/03/2021, Last Change: Never
# Descobre se um triângulo existe de acordo com três medidas e se verdadeiro imprime seu perímetro

a = int(input())
b = int(input())
c = int(input())
n_perimetro = a + b + c

# Tem uma forma mais compacta de fazer os testes mas eu só percebi quando já tinha terminado
teste_1 = a < b + c and b < a + c and c < a + b
teste_2 = a > b - c and b > a - c and c > a - b

if teste_1 and teste_2 == True:
    print('triangulo valido.', n_perimetro)
else:
    print('triangulo invalido.')
