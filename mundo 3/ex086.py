matriz = [[], [], []]
for n in range(3):
    print(f'{n + 1}ª linha: ')
    for i in range(3):
        matriz[n].append(int(input(f'Valor {i+1}ª coluna: ')))
for n in range(len(matriz)):
    for i in range(3):
        print(f'[{matriz[n][i]:^6}]', end='')
    print('')
