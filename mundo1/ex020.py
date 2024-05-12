import random

print('Digite o nome dos integrantes do grupo: ')
name1 = input('aluno 1: ')
name2 = input('Aluno 2: ')
name3 = input('Aluno 3: ')
name4 = input('Aluno 4: ')
lista = [name1, name2, name3, name4]
random.shuffle(lista)
print('A ordem da apresentação será {}'.format(lista))
