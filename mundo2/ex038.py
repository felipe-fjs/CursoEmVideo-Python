print('\033[1;31;46m', '='*10, ' Exercício 038 ', '='*10, '\033[m')
n1 = int(input('Digite Dois número \033[1;31minteiros\033[m: \n'
         'Número 1: '))
n2 = int(input('número 2: '))

if n1 > n2:
    print('O Primeiro valor \033[1;31m({})\033[m é o maior;\n'
          'O valor \033[1;31m({})\033[m é o menor'.format(n1, n2))
elif n2 > n1:
    print(print('O Segundo valor \033[1;31m({})\033[m é o maior;\n'
          'O Primeiro valor \033[1;31m({})\033[m é o menor'.format(n2, n1)))
else:
    print('Ambos valores \033[1;31m({})\033[m e \033[1;31m({})\033[m são iguais!'.format(n1, n2))
