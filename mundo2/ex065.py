cont = 's'
maior = menor = media = quant = soma = 0

while cont == 's':
    quant += 1
    n = int(input(f'\033[1;32;40mDigite o {quant} º número:\033[m '))
    soma += n
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    cont = str(input('Quer continuar? [s/n]  '))
media = soma / quant
print(f'A média entre os {quant} números é {media}')
print(f'O maior número foi \033[1;32m{maior}\033[m\n'
      f'O menor número foi \033[1;31m{menor}\033[m')
