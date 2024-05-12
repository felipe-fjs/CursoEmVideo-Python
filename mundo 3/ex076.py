produtoValor = ('Pão', 4.7, 'Salsicha', 3.15, 'Sorvete', 785, 'Cerveja', 5.55,
                'botijão', 9889.75)
total = 0
print(f'\033[1;97m{'-'*50}\033[m\n'
      f'{'TABELA DE PREÇOS':^50}\n'
      f'\033[1;97m{'-'*50}\033[m')
for ind in range(0, len(produtoValor)):
    if ind % 2 != 0:
        print('', end='')
    else:
        n = produtoValor[ind+1]
        total += n
        if n <= 99:
            n = f'   {n:.2f}'
            print(f'{produtoValor[ind]:.<38}R$ {n:>}')
        elif n <= 999:
            n = f' {n:.2f}'
            print(f'{produtoValor[ind]:.<38}R$ {n:>}')
        else:
            n = f'{n:.2f}'
            print(f'{produtoValor[ind]:.<38}R$ {n:>}')
print(f'\033[1;97;40m{'-'*50}\033[m\n'
      f'\033[1;32m{'Total':.<38}R$ {total:.2f}\033[m')
