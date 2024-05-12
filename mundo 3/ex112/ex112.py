from utilidades import moeda
from utilidades.dado import *
print(f'\033[1;33;40m{' Exercicio 108 ':~^60}\033[m')
valor = leia_dinheiro(input(f'Digite um valor: '))
taxaUp = leia_taxa(input(f'Digite a taxa de aumento: '))
taxaDown = leia_taxa(input('Digite a taxa de diminuição: '))
print(moeda.resumo(valor, taxaUp, taxaDown))
