print(f'\033[1;32m{'=-'*13} Exercicio 075 {'-='*13}\033[m')
valores = []
pares = []
for i in range(0, 4):
    n = int(input(f'Digite o {i+1}º valor: '))
    valores.insert(i, n)
tupla = (valores[0], valores[1], valores[2], valores[3])
print(tupla)
n9 = 0
i3 = None
for i in range(0, len(tupla)):
    if tupla[i] == 9:
        n9 += 1
    if tupla[i] == 3 and i3 is None:
        i3 = i
    if tupla[i] % 2 == 0:
        pares.insert(len(pares), tupla[i])
print(f'\033[1;97;40m{'RESULTADO':-^60}\033[1;97m\033[m\n'
      f'O numero 9 apareceu: \033[1;36m{n9} vezes\033[m')
if i3 is not None:
    print(f'Primeiro 3: posição \033[1;33m{i3+1}\033[m')
else:
    print('O número 3 não apareceu nenhuma vez!')
print(f'Quantos pares: \033[1;32m{pares}\033[m')
