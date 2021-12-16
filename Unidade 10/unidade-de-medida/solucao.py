# (c) amiltoncristian9@gmail.com
# Creation Date: 10-05-2021
# Last Modified: Mon 10 May 2021 14:54:33 -03
# Somar dois valores com unidade de médidas diferentes e retornar o valor em metros

def somar_unidades_distintas(valores, tabela):
    metros_medida_1 = int(valores[0]) * tabela[valores[1]]
    metros_medida_2 = int(valores[2]) * tabela[valores[3]]
    soma_duas_medidas = metros_medida_1 + metros_medida_2
    return soma_duas_medidas


def main():
    tabela_medidas_si = {'km':1000, 'hm':100, 'dam':10,
        'm':1, 'dm':0.1, 'cm':0.01, 'mm':0.001}
    soma_unidades = []

    while True:
        entrada_valores = input().split()
        if entrada_valores[0] == '0' and entrada_valores[2] == '0': break
        soma_unidades.append(somar_unidades_distintas(entrada_valores, tabela_medidas_si))

    for resultado in soma_unidades:
        print(f'{resultado:.2f} m')


if __name__ == "__main__":
    main()
