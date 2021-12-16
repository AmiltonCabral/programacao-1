# (py) amiltoncristian9@gmail.com
# Date: 16/03/2021, Last Change: Never
# Calcular o perímetro de um triangulo a partir de 
# ... 3 pontos no plano cartesiano

n_a_x = int(input())
n_a_y = int(input())
n_b_x = int(input())
n_b_y = int(input())
n_c_x = int(input())
n_c_y = int(input())

# Dab = ((Xa - Xb) ** 2 + (Ya - Yb) ** 2) ** 0.5

n_distancia_ab = ((n_a_x - n_b_x) ** 2 + (n_a_y - n_b_y) ** 2) ** 0.5
n_distancia_ac = ((n_a_x - n_c_x) ** 2 + (n_a_y - n_c_y) ** 2) ** 0.5
n_distancia_bc = ((n_b_x - n_c_x) ** 2 + (n_b_y - n_c_y) ** 2) ** 0.5

n_perimetro_abc = n_distancia_ab + n_distancia_ac + n_distancia_bc

print(f'O perímetro é de {n_perimetro_abc:.2f}')
