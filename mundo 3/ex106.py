def linha(frase, fim=False):
    if not fim:
        print('\033[1;34m', '~'*(len(frase)+30), '\033[m')
        print(f'\033[1;34m{' '*15}\033[4m{frase}\033[m')
        print('\033[1;34m', '~'*(len(frase)+30), '\033[m')
    else:
        print('\033[1;31m', '~' * (len(frase) + 30), '\033[m')
        print(f'\033[1;31m{' ' * 15}\033[4m{frase}\033[m')
        print('\033[1;31m', '~' * (len(frase) + 30), '\033[m')


def funcao_help():
    from time import sleep
    while True:
        linha('Sistema de ajuda PyHelp')
        funcao = input('Informe uma Função ou Biblioteca: ')
        if funcao.upper() in 'FIM':
            linha('FIM DO PROGRAMA', True)
            break
        else:
            print(f'\033[1;97m{' Acessando Manual do comando ' + funcao + ' ':~^55} \033[m')
            sleep(1)
            print('\033[1;97m')
            help(funcao)
            print('\033[m', end='')
            sleep(1)


funcao_help()
