# (py) amiltoncristian9@gmail.com
# Creation Date: 10-04-2021
# Last Modified: sáb 10 abr 2021 21:05:40
# Detectar o momento em que o a caixa preta recebe valores inválidos e contar quantos dados válidos recebey

peso, combustivel, altitude = 0, 0, 0

while True:
    dados = input().split()
    
    if int(dados[0]) < 0:
        print('dado inconsistente. peso negativo.')
        break
    else:
        peso += 1

    if int(dados[1]) < 0:
        print('dado inconsistente. combustível negativo.')
        break
    else:
        combustivel += 1

    if int(dados[2]) < 0:
        print('dado inconsistente. altitude negativa.')
        break
    else:
        altitude += 1

print(f'peso: {peso}')
print(f'combustível: {combustivel}')
print(f'altitude: {altitude}')
