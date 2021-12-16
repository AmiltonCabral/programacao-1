# (py) amiltoncristian9@gmail.com
# Date: 12/03/2001, Last Change: Never
# Calcula cateto a partir da hipotenusa e outro cateto

n_hip = float(input('hipotenusa? '))
n_cat1 = float(input('cateto? '))

# hip² = ca² + co²
# co² = hip² - ca²

n_cat2 = (n_hip ** 2 - n_cat1 ** 2) ** 0.5

print(f'hipotenusa: {n_hip:.2f}')
print(f'cateto 1: {n_cat1:.2f}')
print(f'cateto 2: {n_cat2:.2f}')
