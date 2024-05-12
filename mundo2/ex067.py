print(f'\033[1;32;97m {'=-'*12} Exercicio 067 {'-='*12} \033[m')
while True:
    n = int(input(f'Digite um número para a tabuada [negativo para parar]: '))
    if n < 0:
        break
    print('Soma    - Subtração    - Divisão       - Multiplicação\n')
    for c in range(1, 11):
        print(f'\033[1;31m{n}+{c} = {n+c}\033[m  |\033[1;32m {n}-{c}= {n-c}\033[m   | \033[1;33m{n}x{c} = {n*c}\033[m'
              f' |  \033[1;34m{n}/{c}={n/c:.2f}\033[m')
print('Programa interrompido')
