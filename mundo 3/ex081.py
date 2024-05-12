print(f'\033[1;33;40m{'='*15} Exercicio 081 {'='*15}\033[m')
nums = list()
quant = 0
while True:
    n = float(input(f'Digite o {quant+1} número: '))
    nums.append(n)
    quant += 1
    cont = str(input('Quer continuar? [S/N] '))
    if cont in 'Nn':
        break
nums.sort(reverse=True)
cinco = 'O valor 5 foi digitado na lista!' if 5 in nums else 'O numero 5 não foi digitado!'
print(f'Quantidade de números: {quant}\n'
      f'Lista em ordem decrescente: {nums}\n'
      f'{cinco}')
