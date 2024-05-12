import datetime
print('\033[1;31;40m', '=-'*15, ' Exercicio 054 ', '=-'*15, '\033[m')
ano = datetime.date.today().year
s = 0
for c in range(0, 7):
    print('{}ª Pessoa:'.format(c+1))
    nasc = int(input('Digite seu ano de nascimento: '))
    if ano - nasc >= 18:
        print('Essa pessoa tem {} ano(s), já é maior de idade!'.format(ano - nasc))
        s += 1
    else:
        print('Essa pessoa tem {} ano, ainda não é maior de idade!'.format(ano - nasc))
print('{} pessoa(s) são maiores de idade'.format(s))
