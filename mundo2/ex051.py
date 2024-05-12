print('\033[1;32;40m', '=-'*15, ' Exercicio 051 ', '=-'*15, '\033[m')
a1 = float(input('Digite o valor do primeiro termo da P.A: '))
r = float(input('Digite a razão da P.A: '))
for c in range(1, 11):
    a = a1 + (c-1)*r
    print('{}ª termo da P.A: {}'.format(c, a))
