vel = int(input('Digite a velocidade: '))
if vel > 80:
    multa = (vel-80)*7
    print('Você ultrapassou a velocidade permitida de 80 km/h.\n'
          'Sua multa ficou no valor de R$ {:.2f} reais'.format(multa))
else:
    print('Parabéns! Você está dentro do limite permitido de 80 km/h')

