from utilidades import moeda
from utilidades.dado import leia_dinheiro
print(f'\033[1;33;40m{' Exercicio 108 ':~^60}\033[m')
valor = float(leia_dinheiro(input(f'Digite um valor: ').replace(',', '.')))
taxaUp = float(input(f'Digite a taxa de aumento: ').replace(',', '.'))
taxaDown = float(input('Digite a taxa de diminuição: '))
print(moeda.resumo(valor, taxaUp, taxaDown))
