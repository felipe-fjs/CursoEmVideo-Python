lim = int(input('DIgite a quant de números: '))
x = 0
y = 1
inter = 0
cont = 0
while cont < lim:
    print('{}'.format(x), end='-> ')
    inter = y
    y = x + y
    x = inter
    cont += 1
print('Fim do código!')
