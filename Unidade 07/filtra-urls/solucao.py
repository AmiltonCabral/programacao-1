# (py) amiltoncristian9@gmail.com
# Creation Date: 20-04-2021
# Last Modified: ter 20 abr 2021 16:20:50
# Detectar sites do google

def filtra_urls(lista_links):
    google, links_google = 'google.com', []
    for link in lista_links:
        i, confirmacao = 0, ''
        for letra in link:
            if letra == google[i]:
                i += 1
                confirmacao += letra
            elif letra == google[0]:
                i = 1
                confirmacao = 'g'
            else:
                i = 0
                confirmacao = ''
            if google == confirmacao:
                links_google.append(link)
                break
    return links_google


p1 = ['google.comgoogle.com', 'www.uol.com', 'google', '.com', 'googlegoogle.com', 'www.google.com','http://mail.google.com']
print(filtra_urls(p1))
