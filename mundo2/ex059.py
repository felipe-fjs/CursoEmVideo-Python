import time

print('\033[1;37;40m', '=-'*15, ' Exericcio 059 ', '-='*15, '\033m')
n1 = int(input('Digite dois valores: \n'
               'Número 1: '))
n2 = int(input('Número 2: '))
option = 0
while option != 5:
    print('\033[1;31;40m', '-'*15, ' OPÇÕES ', '-'*15, '\033[m')
    option = int(input('Qual operação você quer realizar? \n'
                       '[1] Somar\n'
                       '[2] Multiplicar\n'
                       '[3] Informar o maior\n'
                       '[4] Digitar novos valores\n'
                       '[5] Sair do programan\n'))
    print('\033[1;31;40m', '-' * 15, ' FIM DAS OPÇÕES ', '-' * 15, '\033[m')
    if option == 1:
        print('=-'*12, ' \033[1;32;40mSOMA\033[m ', '-='*12)
        soma = n1 + n2
        print('A soma entre {} e {} é {}'.format(n1, n2, soma))
        print('=-' * 12, '\033[1;31;40mFIM DA SOMA\033[m ', '-=' * 12)
    elif option == 2:
        print('=-' * 12, ' \033[1;32;40mMULTIPLICAÇÃO\033[m ', '-=' * 12)
        mult = n1 * n2
        print('A multiplicação entr e{} e {} é {}'.format(n1, n2, mult))
        print('=-' * 12, ' \033[1;31;40mFIM DA MULTIPLICAÇÃO\033[m ', '-=' * 12)

    elif option == 3:
        print('=-' * 12, ' \033[1;32;40mMAIOR NÚMERO\033[m ', '-=' * 12)
        maior = max([n1, n2])
        print('O maior número entre {} e {} é {}!'.format(n1, n2, maior))
        print('=-' * 12, ' \033[1;31;40m FIM DE MAIOR NÚMERO\033[m ', '-=' * 12)
    elif option == 4:
        print('=-' * 12, ' \033[1;32;40mDIGITAR NOVOS NÚMEROS\033[m ', '-=' * 12)
        n1 = int(input('Número 1: '))
        n2 = int(input('Número 2: '))
        print('=-' * 12, ' \033[1;32;40mFIM DE DIGITAR NOVOS NÚMEROS\033[m ', '-=' * 12)
    time.sleep(1)
print('Você saiu do programa!')

