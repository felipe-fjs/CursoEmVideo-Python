nome = input('Digite seu nome completo: ').split()
firstName = nome[0]
lastName = nome[len(nome)-1]
print('Primeiro nome: {}\n'
      'Ultimo nome: {}'.format(firstName, lastName))
