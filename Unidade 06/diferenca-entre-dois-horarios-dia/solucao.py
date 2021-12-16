# (py) amiltoncristian9@gmail.com
# Creation Date: 13-04-2021
# Last Modified: seg 19 abr 2021 11:45:08
# Calcula a diferença de horarios

def quanto_tempo(horario1, horario2):
    tempo1 = horario1.split(':')
    tempo2 = horario2.split(':')
    hora1_min1 = int(tempo1[0]) * 60
    hora2_min2 = int(tempo2[0]) * 60
    minuto1 = hora1_min1 + int(tempo1[1])
    minuto2 = hora2_min2 + int(tempo2[1])
    hora = (minuto2 - minuto1) // 60
    minutos = (minuto2 - minuto1) % 60
    saida = f'{hora} hora(s) e {minutos} minuto(s)'
    return saida
