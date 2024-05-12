print('\033[1;32;40m', '=-'*15, ' Exercicio 052 ', '=-'*15, '\033[m')
n = int(input('Digite um número: '))
quant = 0
print('O número {} foi divisível por: '.format(n))
for c in range(1, n+1):
    if n % c == 0:
        print('{} '.format(c), end='-> ')
        quant += 1
print('ACABOU!!')

if quant == 2:
    print('O número {} é primo!')
