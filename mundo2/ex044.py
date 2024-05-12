valor = float(input('Digite o valor do produto: '))
pay_form = int(input('Escolha a forma de pagamento:\n'
                     '(1) \033[1;97mÀ vista em Dinheiro\033[m: 10% de desconto;\n'
                     '(2) \033[1;97mÀ vista no Cartão\033[m: 5% de desconto;\n'
                     '(3) \033[1;97mAté 2x no cartão\033[m: preço normal\n'
                     '(4) \033[1;97m3x ou mais\033[m: 20% de juros\n'))
print('\033[1;30;42m', '='*30, '\033[m')
if pay_form == 1:
    preco = valor * 0.9
    print('\033[1;33;40mValor do produto\033[m: \033[1;31mR$ {:.2f}\033[m\n'
          '\033[1;33;40mValor a ser pago \033[1;32m(10% de desconto)\033[m : \033[1;31mR$ {:.2f}\033[m'.format(valor, preco))
elif pay_form == 2:
    preco = valor * 0.95
    print('\033[1;33;40mValor do produto\033[m: \033[1;31mR$ {:.2f}\033[m\n'
          '\033[1;33;40mValor a ser pago \033[1;32m(5% de desconto)\033[m : \033[1;31mR$ {:.2f}\033[m'.format(valor, preco))
elif pay_form == 3:
    print('\033[1;33;40mValor do produto\033[m: \033[1;31mR$ {:.2f}\033[m em até 2x (R$ {:.2f})'.format(valor, valor/2))
elif pay_form == 4:
    preco = valor * 1.2
    print('\033[1;33;40mValor do produto\033[m: \033[1;31mR$ {:.2f}\033[m\n'
          '\033[1;33;40mValor a ser pago \033[1;31;40m(20% de juros)\033[m : \033[1;31mR$ {:.2f}\033[m\n'
          'Parcelas: \n'
          '     * 3x: R$ {:.2f}\n'
          '     * 4x: R$ {:.2f}'.format(valor, preco, preco/3, preco/4))
