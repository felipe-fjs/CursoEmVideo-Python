print('\033[1;31;40m', '=-'*15, ' Exercicio 048 ', '=-'*15, '\033[m')

s = 0
quant = 0
for c in range(0, 501):
    if c % 2 != 0 and c % 3 == 0:
        s += c
        quant += 1
print("A quantidade de \033[1;31;40mnúmeros ímpares e múltiplos de 3\033[m é igual \033[1;32m{}\033[m\n"
      "E sua soma à \033[1;32;40m{}\033[m".format(quant, s))
