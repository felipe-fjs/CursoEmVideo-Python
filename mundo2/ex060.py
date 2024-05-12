print('\033[1;32;40m', '=-' * 15, ' Exercicio 060 ', '-=' * 15, '\033[m')
n = int(input('Digite um número \033[1;31minteiro\033[m: '))
fatorial = 1
print('Calculando o fatorial do Número {}'.format(n), end='= ')
for c in range(n, 0, -1):
    fatorial = fatorial * c
    if c != 1:
        print('{}'.format(c), end='x')
    else:
        print('{} = {}'.format(c, fatorial))

print('O fatorial do número \033[1;32m{}\033[m é \033[1;4;97m{}\033[m'.format(n, fatorial))

n = int(input('Digite o numero: '))
fat = 1
