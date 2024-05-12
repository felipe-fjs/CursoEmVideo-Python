import random
import time
print(f'\033[1;33m{'='*20} Exercicio 088 {'='*20}\033[m')
print(f'{'MEGA SENA'::^55}')
jogos = list()
jogo = list()
quant = int(input('Quantos jogos serão gerados? '))
for i in range(quant):
    for c in range(6):
        n = random.randint(1, 60)
        if n in jogo:
            while n in jogo:
                n = random.randint(1, 60)
            jogo.append(n)
        else:
            jogo.append(n)
    jogos.append(jogo[:])
    jogo.clear()
for i in range(len(jogos)):
    time.sleep(0.5)
    jogos[i].sort()
    print(f'\033[1;31mJogo {i+1}:\033[m\033[1;32m ', end='')
    for c in range(6):
        print(f'{jogos[i][c]}', end=' ')
    print('\033[m')
print(f'\033[1;33m{'='*55}')
