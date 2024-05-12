print('\033[1;33;40m', '='*10, ' Exercicio 043', '='*10, '\033[m')
peso = float(input('Digite o seu peso em KG: '))
alt = float(input('Digite sua altura em m: '))
imc = peso/alt**2
if imc < 18.5:
    print('Seu IMC é \033[1;97m{:.2f}\033[m. \n'
          'Você está \033[1;31mabaixo do peso\033[m ideal!!!'.format(imc))
elif imc < 25:
    print('Seu IMC é \033[1;97m{:.2f}\033[m\n'
          'Você está na faixa de peso ideal!')
elif imc < 30:
    print('Seu IMC é \033[1;31m{:.2f}\033[m.\n'
          'Você está com \033[31mSOBREPESO\033[m'.format(imc))
elif imc < 40:
    print('Seu IMC é \033[1;31m{:.2f}\033[m.\n'
          'Você está com \033[1;31mOBESIDADE\033[m'.format(imc))
else:
    print('Seu IMC é \033[1;31m{:.2f}\033[m.\n'
          'Você está com \033[1;31;40mOBESIDADE MORBIDA\033[m'.format(imc))
