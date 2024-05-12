print('\033[1;30;107m', '='*10, ' Exercicio 041 ', '='*10, '\033[m')
idade = int(input('Digite sua idade: '))
if idade <= 9:
    print('Você é um nadador \033[1;32mMIRIM\033[m')
elif idade <= 14:
    print('Você é um nadador \033[1;34mINFANTIL\033[m')
elif idade <= 19:
    print('Você é um nadador \033[1;36mJUNIÔR\033[m')
elif idade == 20:
    print('Você é um nadador \033[1;31mSÊNIOR\033[m')
else:
    print('Você é um nadador \033[1;97mMASTER\033[m')
