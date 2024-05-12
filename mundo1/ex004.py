ent = input('Digite algo:')
tipo = type(ent)
justNumber: bool = ent.isnumeric()
isAlphNum = ent.isalnum()
isSpace = ent.isspace()
justAlpha = ent.isalpha()

isNull = bool(ent)
print('O valor digitado "{}", possui as seguintes informaçãos:'.format(ent))
print('O tipo de {} é: {}\n'
      'Só possui número? {}\n'
      'É um Alpha-númerico? {}\n'
      'Possui espaço? {}\n'
      'Só tem letras? {}\n'
      'Possui valor dentro? {}'.format(ent, tipo, justNumber, isAlphNum, isSpace, justAlpha, isNull))
