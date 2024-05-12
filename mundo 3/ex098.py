from time import sleep


def contadorpers(ini, fim, passo: int):
    if ini > fim and passo > 0:
        passo = - passo
    if passo == 0:
        passo = 1
    print('CONT PERSONALIZADO: ', end='')
    sleep(1.5)
    for i in range(ini, fim+1, passo):
        print(f'{i}', end='->')
        sleep(0.75)
    print('\033[1;31mFIM CONT PERSONALIZADO\033[m')
    print(f'\033[1;33m{'FIM':~^40}\033[m')


def cont_padrao():
    print('CONT 1: ', end='')
    sleep(1.5)
    for i in range(1, 11, 1):
        print(f'{i}', end='->')
        sleep(0.75)
    print(f'\033[1;32mFIM CONT 1\033[m')
    sleep(1.5)
    print('CONT 2: ', end='')
    for ind in range(10, 0, -2):
        print(f'{ind}', end='->')
        sleep(0.75)
    print('\033[1;32mFIM CONT 2\033[m')
    print(f'\033[1;31m{' FIM CONT PADRÃO ':=^40}\033[m')
    sleep(2)


print(f'{' Exercicio 098 ':-^40}')
cont_padrao()
contadorpers(int(input('Inicio: ')), int(input('Fim: ')), int(input('Valor dos passos: ')))
