n = int(input('Digite um número: '))
resto = n % 2
if resto == 0:
    par = 'par'
else:
    par = 'impar'
print('O número {} é: {}'.format(n, par))
