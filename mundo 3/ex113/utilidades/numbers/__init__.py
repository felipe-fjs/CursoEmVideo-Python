def leia_int(n):
    valido = False
    while not valido:
        try:
            n = int(n)
        except (TypeError, ValueError, AttributeError):
            print('\033[1;31mERRO! Digite um número inteiro válido!\033[m')
            n = input('Digite m número inteiro: ')
        except KeyboardInterrupt:
            print('O usuário decidiu não digitar o número')
        else:
            valido = True
    return n


def leia_float(n):
    valido = False
    while not valido:
        try:
            n = float(n)
        except ValueError:
            print('\033[1;31mERRO! Digite um Float válido!\033[m')
            n = input('Digite um número real:')
        except KeyboardInterrupt:
            print('\033[1;31mO usuário decidiu não informar o número: ')
        else:
            valido = True
    return n

