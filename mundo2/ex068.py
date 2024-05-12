import random
print(f'\033[1;97;40m{'='*50}\033[m\n'
      f'{'VAMOS JOGAR PAR OU IMPAR':^50}\n'
      f'\033[1;97;40m{'='*50}\033[m')

partida = 0
while True:
    if partida != 0:
        print(f'\033[1;31;40m{'-'*35}\033[m')
    partida += 1
    mao = str(input('Informe sua mão [par/impar]: '))
    nH = int(input('Digite um número: '))
    nPc = random.randint(0, 11)
    soma = nPc + nH
    if soma % 2 == 0:
        if mao == 'par':
            print(f'Você venceu!\n'
                  f'Você jogou {nH} e o PC {nPc}, dando {soma} que é par!')
            print('\033[1;33mVAMOR JOGAR NOVAMENTE...\033[m')
        else:
            print("GAME OVER!\n"
                  f"Você ganhou {partida - 1} vezes.\n"
                  f"O PC ganhou {partida - (partida - 1)}")
            break
    else:
        if mao == 'impar':
            print(f'Você venceu!\n'
                  f'Você jogou {nH} e o PC {nPc}, dando {soma} que é ímpar!')
        else:
            print("GAME OVER!\n"
                  f"Você ganhou {partida - 1} vezes."
                  f"O PC ganhou {partida - (partida - 1)}")
            break

