print(f'\033[1;32;40m {'='*20} Exercicio 085 {'='*20} \033[m')
nums = [[], []]
for i in range(7):
    n = int(input(f'Digite o {i+1} número: '))
    if n % 2 == 0:
        nums[0].append(n)
    else:
        nums[1].append(n)
nums[0].sort()
nums[1].sort()
print(f'\033[m\033[m\n'
      f'Número pares: {nums[0]}\n'
      f'NUmeros impares: {nums[1]}')
