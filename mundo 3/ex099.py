from random import randint


def maiornum(*num):
    maior = 0
    for i in range(len(num)):
        if i == 0:
            maior = num[i]
        elif num[i] > maior:
            maior = num[i]
    print(f'O maior número dos {len(num)} valores {num} é {maior}')


def maioraleatorio(quant):
    nums = []
    maior = 0
    for i in range(quant):
        nums.append(randint(0, 100))
    print(f'Números sorteados: {nums}')
    for i in range(len(nums)):
        if i == 0:
            maior = nums[i]
        elif nums[i] > maior:
            maior = nums[i]
    print(f'O maior número sorteado foi {maior}!')


print(f'\033[1;33m{' Exercicio 099 ':=^50}\033[m')
maiornum(1, 7, 5, 6)
maioraleatorio(4)
print(f'\033[1;31m{' FIM ':=^50}\033[m')
