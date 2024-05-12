nome = input('Digite seu nome completo: ').strip()
nomeSplit = nome.split()
nomeUpper = nome.upper()
nomeLower = nome.lower()
nCarac = len(nome.replace(' ', ''))
nFirst = len(nomeSplit[0])
print('Maiúsculas: {}\n'
      'Minúsculas: {}\n'
      'Quant. letras sem espaço: {}\n'
      'Letras primeiro nome: {}'.format(nomeUpper, nomeLower, nCarac, nFirst))
