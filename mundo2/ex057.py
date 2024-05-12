print('\033[1;33;40m', '-='*15, ' Exercicio 057 ', '-='*15, '\033[m')
sexo = ''
while sexo not in ['M', 'F']:
    sexo = str(input('Digite o seu sexo [M/F]: ')).upper()
    if sexo not in ['M', 'F']:
        print('VALOR INVALIDO!\n'
              'Digite M ou F!')
print('Acabou!')

