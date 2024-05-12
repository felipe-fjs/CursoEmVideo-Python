n1 = float(input('Digite o 1º número: '))
n2 = float(input('2º número: '))
n3 = float(input('3º número: '))
lista = [n1, n2, n3]

print('O maior valor é: {}\n'
      'O menor valor é: {}'.format(max(lista), min(lista)))
# n1Maiorn2 = n1 > n2
# n1Maiorn3 = n1 > n3
# n2Maiorn3 = n2 > n3
###if n1Maiorn2:
###    if n1Maiorn3:
###        maior = n1
###    else:
###        maior = n3
###    if n2Maiorn3:
###        menor = n3
###    else:
###        menor = n2
###elif n2Maiorn3:
###    maior = n2
###    if n1Maiorn3:
###        menor = n3
###    else:
###        menor = n1
###else:
###    maior = n3
###    menor = n1

###print('O MAIOR número é {} e o MENOR é {}'.format(maior, menor))
