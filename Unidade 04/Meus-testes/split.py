# (py) amiltoncristian9@gmail.com
# Date: , Last Change: Never
# isso é apenas um teste

entrada = '123123'
#def plit_com_espaco(entrada):
tokens = entrada.split(", ") # este argumento tem espaço!
num1 = int(tokens[0])
num2 = int(tokens[1])
print(num1, num2)

#def split_sem_espaco(entrada):
tokens = entrada.split(",") # argumento não tem espaço
num1 = int(tokens[0])
num2 = int(tokens[1])
print(num1, num2)
