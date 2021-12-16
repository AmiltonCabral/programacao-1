# (py) amiltoncristian9@gmail.com
# Date: 01/04/2021, Last Change: Never
# Descobrir qual sequência tem o maior desvio padrão

a = input()
b = input()

sequencia_a = a.split()
sequencia_b = b.split()
media_a = 0
media_b = 0
n_a = len(sequencia_a)
n_b = len(sequencia_b)
E_a = 0
E_b = 0

for i in sequencia_a:
    media_a = media_a + float(i)
media_a = media_a / n_a

for i in sequencia_b:
    media_b = media_b + float(i)
media_b = media_b / n_b

for i in sequencia_a:
    E_a += ((float(i) - media_a) **2)

for i in sequencia_b:
    E_b += ((float(i) - media_b) **2)

resultado_a = (E_a / (n_a -1)) **0.5
resultado_b = (E_b / (n_b -1)) **0.5

if resultado_a > resultado_b:
    print(f'A sequência 1 possui o maior desvio padrão ({resultado_a:.2f}).')
elif resultado_b > resultado_a:
    print(f'A sequência 2 possui o maior desvio padrão ({resultado_b:.2f}).')
elif resultado_a == resultado_b:
    print(f'As sequências possuem o mesmo desvio padrão ({resultado_a:.2f}).')
