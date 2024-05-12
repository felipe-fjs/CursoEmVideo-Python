import random
import time

mao = ['pedra', 'papel', 'tesoura']
n = int(input('Escolha:\n'
              '(0) Pedra\n'
              '(1) Papel\n'
              '(2) Tesoura\n'
              'Qual sua esoclha? '))
player = mao[n]
pc = random.choice(['pedra', 'papel', 'tesoura'])

print('JO')
time.sleep(0.4)
print('KEN')
time.sleep(0.4)
print('PO!')
time.sleep(0.5)

print('\033[1;31;40m', '=-'*18, '\033[m')
print('Computador jogou \033[1;36m{}\033[m'.format(pc))
print('jogador jogou \033[1;33m{}\033[m'.format(player))
print('\033[1;31;40m', '=-'*18, '\033[m')

if player == 'pedra':
    if pc == 'pedra':
        print('\033[1;97mDeu empate!\033[m')
    elif pc == 'papel':
        print('Computador \033[1;32mGanhou\033[m!\n'
              'jogador \033[1;31mperdeu\033[m!')
    else:
        print('Computador \033[1;31mPerdeu\033[m\n'
              'jogador \033[1;32mGanhou\033[m!')
elif player == 'papel':
    if pc == 'pedra':
        print('Computador \033[1;31mPerdeu\033[m\n'
              'jogador \033[1;32mGanhou\033[m!')
    elif pc == 'papel':
        print('\033[1;97mDeu empate!\033[m')
    else:
        print('Computador \033[1;32mGanhou\033[m\n'
              'jogador \033[1;31mPerdeu\033[m!')
elif player == 'tesoura':
    if pc == 'pedra':
        print('Computador \033[1;32mGanhou\033[m\n'
              'jogador \033[1;31mPerdeu\033[m!')
    elif pc == 'papel':
        print('Computador \033[1;31mPerdeu\033[m\n'
              'jogador \033[1;32mGanhou\033[m!')
    else:
        print('\033[1;97mDeu empate!\033[m')