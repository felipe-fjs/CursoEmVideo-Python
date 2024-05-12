from random import choice

name1 = input('Digite o nome do primeiro aluno:')
name2 = input('Digite o nome do segundo aluno: ')
name3 = input('Digite o nome do terceiro aluno: ')
name4 = input('Digite  o nome do quarto aluno: ')
lista = [name1, name2, name3, name4]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))
