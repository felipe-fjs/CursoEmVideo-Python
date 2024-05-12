print('\033[1;36;41m='*10, ' DESAFIO 36 ', '='*10, '\033[m')
valueHouse = float(input('Digite o valor total da casa: '))
sal = float(input('Digite  o salário \033[1;31mmensal\033[m do comprador: '))
tempo = int(input('Digite em quantos anos será paga a casa: '))

mensal = valueHouse / (tempo*12)

if mensal > (0.3 * sal):
    print('Infelizmente seu empréstimo foi \033[31mnegado\033[m, pois a mensalidade que é de R$ {:.2f}'
          ' é maior que 30% do seu salário R$ {:.2f}'.format(mensal, (0.3*sal)))
else:
    print('\033[1;34[mParabéms!\033[m Seu empréstimo foi aprovado, pois a mensalidade de R$ {:.2f}'
          ' é menor que 30% do seu salário R$ {:.2f}'.format(mensal, 0.3*sal))
