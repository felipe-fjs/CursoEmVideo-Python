from random import randint
maior = menor = 0
tupla = (randint(0, 100), randint(0, 100), randint(0, 100),
         randint(0, 100), randint(0, 100))

for c in range(0, len(tupla)):
    if c == 0:
        maior = menor = tupla[c]
    else:
        if tupla[c] > maior:
            maior = tupla[c]
        if tupla[c] < menor:
            menor = tupla[c]

print(f'Tupla inteira: {tupla}\n'
      f'maior numero: {maior}\n'
      f'menor numero: {menor}')
