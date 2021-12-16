# (py) amiltoncristian9@gmail.com
# Date: 16/03/2021, Last Change: Never
# Calcular quantas páginas são necessárias para visualizar os tweets

n_quantidade_tts = int(input())

n_paginas = n_quantidade_tts // 400
n_resto_tts = n_quantidade_tts % 400
n_tts_perdidos = (n_resto_tts * 100) / n_quantidade_tts

print(f'Serão necessárias {n_paginas} página(s) para visualizar os tweets.')
print(f'{n_tts_perdidos:.1f}% dos tweets serão perdidos.')
