
# Last Modified: qua 14 abr 2021 09:32:02
# Calcula a diferença de horarios

horario1 = '01:55'
horario2 = '02:03'

#def quanto_tempo(horario1, horario2):
tempo1 = horario1.split(':')
tempo2 = horario2.split(':')
#hora = int(tempo2[0]) - int(tempo1[0])
minutos = (int(tempo2[1]) - int(tempo1[1])) % 60
saida = f'{hora} hora(s) e {minutos} minuto(s)'
#return saida

print(saida)


