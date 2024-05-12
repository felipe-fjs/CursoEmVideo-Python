import random
nPc = random.randint(0, 10)

print('\033[32;40m', '=-'*15, ' Exercicio 058 ', '-='*15, '\033[m')
nHm = -1
attempts = 0
print('\033[1;31;40m', '='*10, ' Tente advinhar o número que o Computador pensou! ', '='*10, '\033[m')

while nHm != nPc:
    attempts += 1
    nHm = int(input('{}ª Tentativa, figite um número de 0 a 10:'.format(attempts)))
    if nHm == nPc:
        print('\033[1;32;40mParabéns!\033[m Você acertou o número que o computador pensou!')
        if attempts > 1:
            print('Você precisou de {} tentativas para acertar o número!'.format(attempts))
        else:
            print('Você precisou de apenas {} tentativa para acertar o número!'.format(attempts))
    else:
        print('Que pena! Você errou!')
        print('='*15)

