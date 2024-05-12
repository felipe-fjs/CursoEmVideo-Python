from random import randint

dic = dict()


def soma(num):
    s = 0
    pares = []
    print(f'\033[1;33mSomando os pares: ', end='')
    for i in range(len(num)):
        if num[i] % 2 == 0:
            pares.append(num[i])
    if len(pares) != 0:
        for i in range(len(pares)):
            s += pares[i]
            if i == len(pares) - 1:
                print(f'{pares[i]}', end=' = ')
            else:
                print(f'{pares[i]}', end=' + ')
        print(f'{s}\033[m')
    else:
        print(f'\033[1;31mNão foram sorteador números pares!\033')


def sorteia(num):
    print(f'\033[1;32mSorteados: ', end='')
    for i in range(5):
        nums.append(randint(1, 100))
        print(f'{nums[i]}', end='->')
    print('\033[4mFIM\033[m')
    soma(num)


print(f'\033[1;36m{' Exercicio 100 ':=^50}\033[m')
nums = []
sorteia(nums)
