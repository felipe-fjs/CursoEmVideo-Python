print('\033[1;31;42m', '='*10, ' Exercicio 42 ', '='*10, '\033[m')
lado1 = float(input('Digite 3 retas:\n'
                    'Reta/Lado 1: '))
lado2 = float(input('Reta/Lado 2: '))
lado3 = float(input('Reta/Lado 3: '))
tipo = 'Escaleno'
if lado1 < lado2 + lado3 and lado2 < lado3 + lado1 and lado3 < lado2 + lado1:
    print('As retas \033[1;32mpodem\033[m formar um triângulo!!')
    if lado1 == lado2 == lado3:
        tipo = 'Equilátero'
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        tipo = 'Isósceles'
    print('O tipo de triângulo que as 3 retas formam é um triângulo \033[1;97;40m{}\033[m'.format(tipo.upper()))
else:
    print('As retas \033[1;31mnão podem\033[m formar um triângulo!')
