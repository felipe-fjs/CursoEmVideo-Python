from moduls import moeda

val = float(input('Por favor, digite um valor em R$: '))
print(f'O dobro do valor R$ {moeda.dobro(val)} é R$ {moeda.dobro(val, True):.2f}\n'
      f'A metade do valor R$ {val:.2f} é R$ {moeda.metade(val):.2f}\n'
      f'R$ {val:.2f} + 10% é igual à R$ {moeda.aumentar(val):.2f}\n'
      f'R$ {val:.2f} - 13% é igual à R$ {moeda.diminuir(val):.2f}')
