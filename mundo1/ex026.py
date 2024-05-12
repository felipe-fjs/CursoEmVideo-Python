frase = input('Digite  uma frase: ')
quantA = frase.lower().count('a')
firstA = frase.lower().find('a') + 1
lastA = frase.lower().rfind('a')

print('Quantidade de "a": {}\n'
      'Indice primeiro "a": {}\n'
      'Indice ultimo "a": {}'.format(quantA, firstA, lastA))
