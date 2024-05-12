nums = list()
for c in range(0, 5):
    if c == 0:
        nums.insert(c, int(input(f'Digite o {c+1}º número [: ')))
        print('Adicionado na 1ª posição')
    else:
        num = int(input(f'Digite o {c+1}º número: '))
        for i in range(len(nums)):
            if nums[i] > num:
                nums.insert(i, num)
                print(f'Adicionado na {i+1}ª posição')
                break
        if c == len(nums):
            nums.append(num)
print(nums)
