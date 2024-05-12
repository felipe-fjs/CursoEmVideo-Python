print(f'\033[1;31;40m {'='*12} Exercicio 066 {'='*12} \033[m')
quant = soma = 0
while True:
    n = int(input(f'Digite o {quant+1}º número: '))
    if n == 999:
        break
    quant += 1
    soma += n
print(f'A soma entre os {quant} números é igual à {soma}')
