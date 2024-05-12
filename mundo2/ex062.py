print('\033[1;33;40m', '=-' * 15, ' Exercicio 062 (P.A COM LIMITE VARIÁVEL)', '-=' * 15, '\033[m')
a1 = int(input('Digite o 1º número da P.A: '))
r = int(input('Digite a razão da P.A: '))

cont = 1
an = 1
while cont != 10+1:
    an = a1 + (cont - 1) * r
    print('\033[1;31m{}º\033[m termo = \033[1;32m{}\033[m'.format(cont, an))
    cont += 1
    if cont > 10:
        continuar = str(input('Quer contar mais algum número? [s/n]'))
        if continuar == 's':
            quant = int(input('Quantos? ')) + cont

            while cont <= quant:
                an = a1 + (cont - 1) * r
                print('\033[1;31m{}º\033[m termo = \033[1;32m{}\033[m'.format(cont, an))
                cont += 1
                if cont == quant:
                    print('Fim do código!')
                    quit()
