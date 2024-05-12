print('\033[1;33;40m', '=-'*15, ' Exercicio 053 ', '=-'*15, '\033[m')
palavra = input('DIgite uma palavra: ').replace(' ', '')
inverso = palavra[::-1]
if palavra == inverso:
    print('Essa palavra é um palíndromo!')
else:
    print('Essa palavra não é um palíndromo!\n'
          'palavra: {}\n'
          'Inverso: {}'.format(palavra, inverso))
