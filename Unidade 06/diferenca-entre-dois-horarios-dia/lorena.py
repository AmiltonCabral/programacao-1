def quanto_tempo(horario1, horario2):
    horas1 = f'{horario1[0]}{horario1[1]}'
    minutos1 = f'{horario1[3]}{horario1[4]}'
    horas2 = f'{horario2[0]}{horario2[1]}'
    minutos2 = f'{horario2[3]}{horario2[4]}'
    diferençahora = abs(int(horas2) - int(horas1))
    diferençamin = abs(int(minutos2) - int(minutos1))
    return f'{diferençahora} hora(s) e {diferençamin} minuto(s)'

#assert quanto_tempo("07:15", "09:18") == "2 hora(s) e 3 minuto(s)"

print( quanto_tempo('00:55','01:05') )
