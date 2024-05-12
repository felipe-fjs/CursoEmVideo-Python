print('\033[1;34;107m', '='*10, ' Exercicio 040 ', '='*10, '\033[m')
nota1 = float(input('Digite as duas notas do aluno:\n'
                    'Nota 1:'))
nota2 = float(input('Nota 2: '))
media = (nota1 + nota2)/2
if media <= 5:
    print('Sua média é {:.2f}, você foi \033[1;3mREPROVADO\033[m!!!'.format(media))
elif 5 < media <= 6.99:
    print('Sua média é {:.2f}, você está de \033[1;32mRECUPERAÇÃO\033[m'.format(media))
else:
    print('Sua média é {:.2f}, você está \033[1;34mAPROVADO\033[m!!!'.format(media))
