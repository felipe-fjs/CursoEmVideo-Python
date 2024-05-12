nums = list()
numsPar = list()
numsImpar = list()
cont = 0
while True:
    n = int(input(f'Digite o {cont+1}º número: '))
    if n not in nums:
        nums.append(n)
    continuar = str(input('Deseja continuar? [S/N] '))
    if continuar in 'Nn':
        break
    cont += 1
for ind, c in enumerate(nums):
    if c % 2 == 0 and c != 0:
        numsPar.append(c)
    elif c % 2 != 0:
        numsImpar.append(c)
print(f'Lista completa: {nums}\n'
      f'Lista dos pares: {numsPar}\n'
      f'Lista dos Impares: {numsImpar}')

