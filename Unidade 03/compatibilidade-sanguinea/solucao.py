# (py) amiltoncristian9@gmail.com
# Date: 24/03/2021, Last Change: Never
# Recebe a classificação sanguinia ABO e RH e identifica se a compatibilidade entre o doador e paciente

paciente_abo = input()
paciente_rh = input()
doador_abo = input()
doador_rh = input()

tipo_paciente = paciente_abo + paciente_rh
tipo_doador = doador_abo + doador_rh
resultado = 'incompatível'

if tipo_paciente == 'A+' and (tipo_doador == 'A+' or tipo_doador == 'A-' or tipo_doador == 'O+' or tipo_doador == 'O-'):
    resultado = 'compatível'

elif tipo_paciente == 'A-' and (tipo_doador == 'A-' or tipo_doador == 'O-'):
    resultado = 'compatível'

elif tipo_paciente == 'B+' and (tipo_doador == 'B+' or tipo_doador == 'B-' or tipo_doador == 'O+' or tipo_doador == 'O-'):
    resultado = 'compatível'

elif tipo_paciente == 'B-' and (tipo_doador == 'B-' or tipo_doador == 'O-'):
    resultado = 'compatível'

elif tipo_paciente == 'AB+':
    resultado = 'compatível'

elif tipo_paciente == 'AB-' and (tipo_doador == 'A-' or tipo_doador == 'B-' or tipo_doador == 'AB-' or tipo_doador == 'O-'):
    resultado = 'compatível'

elif tipo_paciente == 'O+' and (tipo_doador == 'O+' or tipo_doador == 'O-'):
    resultado = 'compatível'

elif tipo_paciente == 'O-' and (tipo_doador == 'O-'):
    resultado = 'compatível'


print(resultado)
