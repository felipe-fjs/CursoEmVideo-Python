import datetime
ano = int(input('Digite um ano qualquer (0 para ano atual) : '))
if ano == 0:
    ano = datetime.date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é um ano Bissexto!'.format(ano))
else:
    print('O ano {} não é um ano bissexto!'.format(ano))
