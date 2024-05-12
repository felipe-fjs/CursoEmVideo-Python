def ler_inteiro(n):
    valido = False
    while not valido:
        n = str(n)
        if n.isalpha() or '':
            print(f'\033[1;31mERRO! Digite um NÚMERO INTEIRO!\033[m')
        else:
            return int(n)
        n = input('\033[1;33mDigite sua opção: \033[m')


def linha(tamanho=40):
    return f'\033[1;97m{'-'*tamanho}\033[m'


def cabeçalho(msg: str):
    print(linha())
    print(f'\033[1;97m{msg.center(40)}\033[m')
    print(linha())


def menu(opcoes):
    cont = list(range(1, len(opcoes)+1))
    for ind, value in enumerate(opcoes):
        print(f'\033[1;33m{ind+1} \033[97m-\033[36m {value}\033[m')
    try:
        n = ler_inteiro(input('\033[1;33mDigite sua escolha: \033[m'))
        while n not in cont:
            n = ler_inteiro(input('\033[1;33mDigite um número dentro das opções: \033[m'))
        else:
            return n
    except KeyboardInterrupt:
        print('O usuário decidiu interromper o programa!')
        return len(opcoes)
