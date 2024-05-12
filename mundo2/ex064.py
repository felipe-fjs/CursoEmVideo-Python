ult = 0
soma = 0
quant = 0
print('Para parar a soma, digite o valor "999"!')
while ult != 999:
    soma += ult
    ult = int(input('Digite um valor: '))
    if ult != 999:
        quant += 1
print('A soma dos \033[1;32m{}\033[m números é igual à \033[1;33;40m{}\033[m'.format(quant, soma))
