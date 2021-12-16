# (c) amiltoncristian9@gmail.com
# Creation Date: 28-04-2021
# Last Modified: qua 28 abr 2021 17:40:27
# Descobrir qual o primeiro número que é menor que determinado número

def primeiro_menor(num, numeros):
    menor = -1
    for i in range(len(numeros)):
        if int(numeros[i]) < num:
            menor = i
            break
    return menor


def main():
    sequencia_num = input().split()
    num = int(input())
    indice_primeiro_menor = primeiro_menor(num, sequencia_num)
    if indice_primeiro_menor == -1:
        print(f'sem menores que {num}')
    else:
        valor_primeiro_menor = sequencia_num[indice_primeiro_menor]
        print(f'primeiro menor que {num}: {valor_primeiro_menor}')

    
if __name__ == '__main__':
    main()
