# (py) amiltoncristian9@gmail.com
# Creation Date: 14-04-2021
# Last Modified: qua 14 abr 2021 17:01:53
# Descartar dados inválidos

def conta_alertas_acude(medicoes):
    novas_medicoes = []
    for i in range(1, len(medicoes)):
        if not medicoes[i] - medicoes[i-1] <= -10 and not medicoes[i] - medicoes[i-1] >= 10:
            novas_medicoes.append(medicoes[i])
    print(novas_medicoes)
    alertas = 0
    for i in novas_medicoes:
        if i < 17:
            alertas += 1
    return alertas
