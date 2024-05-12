from math import sqrt
dias = int(input('Quantos dias o carro foi usado? '))
km = int(input('Quantos Quilômettros rodados?'))
total = dias*60 + 0.15*km
print('O valor total a ser pago é: R$ {:.2f} '.format(total))
print(sqrt(total))
