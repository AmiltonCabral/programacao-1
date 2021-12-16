# (py) amiltoncristian9@gmail.com
# Creation Date: 12-04-2021
# Last Modified: seg 12 abr 2021 11:41:09

pos = input().split()
mov = []

while True:
    comando = input()
    if comando == '': break
    mov = comando.split()
    
    if mov[1] == 'h':
        pos[1] = int(pos[1]) - int(mov[0])
    if mov[1] == 'l':
        pos[1] = int(pos[1]) + int(mov[0])
    if mov[1] == 'j':
        pos[0] = int(pos[0]) + int(mov[0])
    if mov[1] == 'k':
        pos[0] = int(pos[0]) - int(mov[0])

    print(f'[{pos[0]} {pos[1]}]')



