matriz = [[], [], []]
somaPares = somaC3 = maior2 = 0
for c in range(3):
    print(f'{c+1}ª fila: ')
    for i in range(3):
        n = int(input(f'Valor {i+1}ª coluna: '))
        matriz[c].append(n)
        if n % 2 == 0:
            somaPares += n
        if i == 2:
            somaC3 += n
        if c == 1:
            if i == 0:
                maior2 = n
            else:
                if n > maior2:
                    maior2 = n
print(f'\033[1;32m{'='*40}\033[m')
for c in range(len(matriz)):
    for i in range(3):
        print(f'[{matriz[c][i]:^6}]', end='')
    print('')
print(f'\033[1;32m{'='*40}\033[m')
print(f'Soma pares: {somaPares}\n'
      f'Soma da 3ª coluna: {somaC3}\n'
      f'Maior da 2ª linha: {maior2}')
