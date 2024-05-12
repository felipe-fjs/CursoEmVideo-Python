n = int(input('Digite um número inteiro: '))
escol = int(input('Será convertido para:\n'
                  '(1) Binário\n'
                  '(2) Octal\n'
                  '(3) Hexadecimal\n'))

if escol == 1:
    nConv = bin(n)
    conv = 'binário'
elif escol == 2:
    nConv = oct(n)
    conv = 'Octal'
elif escol == 3:
    nConv = hex(n)
    conv = 'Hexadecimal'
print('O número {} convertido para {} é igual à : \033[1;31m{}\033[m'.format(n, conv, nConv))
