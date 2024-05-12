sal = float(input('Digite seu salário: '))
if sal <= 1250:
    sal = sal * 1.15
    print('Seu salário foi ajustado em 15% por ser inferior ou igual a R$ 1.250 reais.\n'
          'Agora você receberá {.:2f} reais'.format(sal))
else:
    sal = sal * 1.1
    print('Seu salário foi ajustado em 10% por ser superior R$ 1.250 reais.\n'
          'Agora você receberá {:.2f} reais'.format(sal))

