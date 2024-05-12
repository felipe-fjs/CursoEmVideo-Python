from operator import itemgetter
import random

dic = {}
for n in range(1, 5):
    dic[f'dado{n}'] = random.randint(1, 6)
    print(f'Jogador {n}: {dic[f'dado{n}']}')
rankin = {sorted(dic, key=itemgetter(1), reverse=True)}
print(rankin)
