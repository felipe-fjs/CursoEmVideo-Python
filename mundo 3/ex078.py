print(f'\033[1;33;40m{'='*20} Exercicio 078 {'='*20}\033[m')
nums = list()
for c in range(5):
    nums.append(float(input(f'Digite o {c+1}º valor: ')))
print(f'Os {len(nums)} valores digitados foram: {nums}\n'
      f'Maior numero: {max(nums)} na posição {nums.index(max(nums))+1}\n'
      f'Menor numero: {min(nums)} na posição {nums.index(min(nums))+1}')
print(f'\033[1;33;40m{'='*17} Fim do exercicio 078 {'='*16}\033[m')
