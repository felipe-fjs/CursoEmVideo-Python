from modulos import moeda
print(f'\033[1;33;40m{' Exercicio 108 ':~^60}\033[m')
valor = float(input(f'Digite um valor: ').replace(',', '.'))
taxaUp = float(input(f'Digite a taxa de aumento: ').replace(',', '.'))
taxaDown = float(input('Digite a taxa de diminuição: '))
print(f'O dobro de {moeda.formato(valor)} é {moeda.formato(moeda.dobro(valor))}\n'
      f'Metade de {moeda.formato(valor)} é {moeda.formato(moeda.metade(valor))}\n'
      f'O aumento de {taxaUp}% de {moeda.formato(valor)} é {moeda.aumentar(valor, taxaUp)}\n'
      f'A diminuição de {taxaDown}% no {moeda.formato(valor)} é {moeda.formato(moeda.diminuir(valor, taxaDown))}')