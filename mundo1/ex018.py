from math import radians, sin, cos, tan
ang = float(input('Digite o valor de um Ângulo: '))
rad = radians(ang)
sen = sin(rad)
cos = cos(rad)
tan = tan(rad)

print('O seno, cosseno e tangente do ângulo {} é:\n'
      'Seno: {:.2f}\n'
      'Cosseno: {:.2f}\n'
      'Tangente: {:.2f}'.format(ang, sen, cos, tan))
