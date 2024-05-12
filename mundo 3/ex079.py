nums = list()
while True:
    n = float(input('Digite um novo número ["-1" para parar]: '))
    if n == -1:
        break
    if n not in nums:
        nums.append(n)
nums.sort()
print(f'Os número digitados foram {nums}')
