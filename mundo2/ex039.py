import datetime
print('\033[1;32;107m', '='*10, ' Exercicio 039', '='*10, '\033[m')
nasc = int(input('Digite seu \033[91;7mANO de nascimento\033[m: '))
idade = datetime.date.today().year - nasc
if idade < 18:
    print('Sua idade é {} ano, ainda \033[1;32mnão é hora\033[m de se alistar!'.format(idade))
    print('Faltam {} ano(s) para o seu alistamento!'.format(18-idade))
elif idade == 18:
    print('Sua idade é {} anos, \033[1;32mestá na hora\033[m de se alistar!'.format(idade))
else:
    print('Sua idade é {} anos, \033[1;32mjá passou da hora\033[m de você se alistar!'.format(idade))
    print('Passaram-se \033[1;31m{} ano(s)\033[m do seu alistamento!'.format(idade - 18))
