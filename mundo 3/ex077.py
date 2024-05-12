palavras = ('europa', 'casaquistao', 'ira', 'palavra', 'oceano',
            'brasil', 'portugal', 'alemanha', 'coreia', 'japao')
vogais = []
for ind, item in enumerate(palavras):
    print(f'As vogais da palavra \033[1;31m{item}\033[m são: ', end='')
    for i in range(0, len(item)):
        if item[i] in 'aeiou':
            print(f'\033[1;33m{item[i]}\033[m', end=',')
            if i == len(item) - 1:
                print(f'\033[1;33m{item[i]}\033[m', end='')

    print('')
print('FIM')
