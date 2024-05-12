print('Digite os valores:')
s = 0
cont = 0
for c in range(0, 6):
    n = int(input('\033[1;33;40mDigite o {}º número:\033[m '.format(c+1)))
    if n % 2 == 0:
        s += n
        cont += 1
if cont != 0:
    print('A \033[1;32;40msoma\033[m dos {}  números pares informados '
          'é igual à \033[1;32m{}\033[m1'.format(cont, s))
else:
    print('Você nã digitou nenhum número par!')
