import math
n = int(input('Digite um número entre 0 e 9999: '))
unidade = n % 10
dezena = (n // 10) % 10
centena = (n // 100) % 10
milhar = (n // 1000)

print('unidade: {} \n'
      'Dezenas: {}\n'
      'centenas: {}\n'
      'Milhar: {}'.format(unidade, dezena, centena, milhar))
