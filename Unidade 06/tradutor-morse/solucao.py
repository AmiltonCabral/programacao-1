# (py) amiltoncristian9@gmail.com
# Creation Date: 14-04-2021
# Last Modified: qua 14 abr 2021 15:08:13
# Traduzir um código morse para nosso alfabeto

def tradutor_morse(codificado):
    traduzido = ''
    for i in codificado:
        if i == '.-':
            traduzido += 'a'
        elif i == '-...':
            traduzido += 'b'
        elif i == '-.-.':
            traduzido += 'c'
        elif i == '-..':
            traduzido += 'd'
        elif i == '.':
            traduzido += 'e'
        elif i == '..-.':
            traduzido += 'f'
        elif i == '--.':
            traduzido += 'g'
        elif i == '....':
            traduzido += 'h'
        elif i == '..':
            traduzido += 'i'
        elif i == '.---':
            traduzido += 'j'
        elif i == '-.-':
            traduzido += 'k'
        elif i == '.-..':
            traduzido += 'l'
        elif i == '--':
            traduzido += 'm'
        elif i == '-.':
            traduzido += 'n'
        elif i == '---':
            traduzido += 'o'
        elif i == '.--.':
            traduzido += 'p'
        elif i == '--.-':
            traduzido += 'q'
        elif i == '.-.':
            traduzido += 'r'
        elif i == '...':
            traduzido += 's'
        elif i == '-':
            traduzido += 't'
        elif i == '..-':
            traduzido += 'u'
        elif i == '...-':
            traduzido += 'v'
        elif i == '.--':
            traduzido += 'w'
        elif i == '-..-':
            traduzido += 'x'
        elif i == '-.--':
            traduzido += 'y'
        elif i == '--..':
            traduzido += 'z'
    return traduzido
