numExtenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
              'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
              'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
              'dezenove', 'vinte')
print(f'\033[1;35m{'=-'*15} Exercicio 072 {'-='*15} \033[m')
while True:
    print(f'\033[1;32;40m{'-'*55}\033[m')
    n = int(input('Digite um número entre 0 e 20 [21 para sair]: '))
    while n not in range(0, 22):
        n = int(input('[DIGITE ENTRE 0 E 20] Digite um número entre 0 e 20 [21 para sair]: '))
    if n == 21:
        break
    print(f'Você digitou o número \033[1;33m{numExtenso[n]}\033[m')
print(f'\033[1;40m{'='*20}\033[1;31mFim do programa\033[m\033[1;40m{'='*20}\033[m')
