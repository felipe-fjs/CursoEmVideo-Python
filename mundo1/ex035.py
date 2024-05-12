
print('Digite os valores das retas: ')
reta1 = float(input('Reta 1 = '))
reta2 = float(input('Reta 2 = '))
reta3 = float(input('Reta 3 = '))

if (reta1 < reta2 + reta3) and (reta1 + reta2 > reta3) and (reta1 + reta3 > reta3):
    print('As retas de tamanho {}, {} e {} podem formar um triângulo!'.format(reta1, reta2, reta3))
else:
    print('As retas de tamanho {}, {} e {} não podem formar um triângulo!'.format(reta1, reta2, reta3))
