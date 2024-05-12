import math
catA = float(input('Digite o valor do cateto A:'))
catB = float(input('Digite o valor do cateto B: '))
hip = math.hypot(catA, catB)
print('A hipotenusa do triângulo de catetis {} e {} é igual a {}'.format(catA, catB, hip))
