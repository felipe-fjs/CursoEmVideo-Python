from utilidades.numbers import *

print(f'\033[1;33m{'Exercicio 113':~^50}\033[m')
try:
    n1 = leia_int(input('Digite um número inteiro > 0: '))
    n2 = leia_float(input('Digite um número real > 0: '))
except KeyboardInterrupt:
    print('\n\033[1;31mO usuário decidiu não informar o número\033[m')
else:
    print(f'O número inteiro foi {n1} e o real foi {n2}')
finally:
    print('Obrigado por comparecer, volte sempre!')
