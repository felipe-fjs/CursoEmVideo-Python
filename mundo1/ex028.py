import pygame
import random
nPc = random.randint(0, 5)
nUser = int(input('Escolha um número inteiro entre 1 e 5: '))
print('\033[0:32mProcessando...\033[m')
pygame.time.wait(2500)
if nUser == nPc:
    print('Parabéns, você acertou!!! O número é: {}'.format(nUser))
else:
    print('Que pena. O número correto era {}'.format(nPc))
