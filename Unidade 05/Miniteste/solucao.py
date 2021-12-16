# (py) amiltoncristian9@gmail.com
# Creation Date: 09-04-2021
# Last Modified: sex 09 abr 2021 12:03:11
# Cria um robo que se movimenta em um plano cartesiano, quando y for o dobro de x o jogo acaba e ela encontra o portal

x, y = 0, 0

while True:
    mov = input().split()
    
    if mov[0] == 'E':
        x += -int(mov[1])
    elif mov[0] == 'D':
        x += int(mov[1])
    elif mov[0] == 'C':
        y += int(mov[1])
    elif mov[0] == 'B':
        y += -int(mov[1])
    if mov[1] == '0':
        print('Fim de jogo')
        break

    if x * 2 == y or x * 2 == -y:
        print(f'Parabéns, conquista do portal ({x}, {y})')
        break
