print('\033[1;33;40m', '=-'*15, ' Exercicio 055 ', '=-'*15, '\033[m')
maior = 0.0
menor = 0.0
for c in range(0, 5):
    peso = float(input('Digite o {}º peso: '.format(c+1)))
    if c == 0:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('O maior peso foi \033[1;31m{}\033[m Kg\n'
      'O menor peso foi \033[;1;32m{}\033[m Kg'.format(maior, menor))
