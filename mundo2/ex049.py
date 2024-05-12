print('\033[1;97;40m', '-='*12, ' Desafio 049 ', '-='*12, '\033[m')
n = int(input('Digite o número Inteiro a ser colocado na tabuada: '))

for c in range(0, 11):
    if c == 0:
        print('Soma          Subtração       Multiplicação      Divisão    ')
    else:
        print('{} + {} = {}     {} - {} = {}       {} * {} = {}        {} / = {}  '
              ''.format(n, c, n+c, n, c, n-c, n, c, n*c, n, c, n/c))

