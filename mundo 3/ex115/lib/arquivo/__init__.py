def arquivo_existe(caminho: str):
    try:
        a = open(caminho, 'rt')
        a.close()
    except FileNotFoundError:
        criar = input(f'\033[1;31mArquivo {caminho} não foi encontrado!\033[m\n'
                      f'Deseja criar um arquivo com esse nome? ')
        if criar.strip()[0] in 'Ss':
            try:
                a = open(caminho, 'wt+')
                a.close()
            except Exception as erro:
                erro.__class__()
                print('\033[1;31mERRO! O arquivo não foi criado!\033[m')
                return False
            else:
                print(f'O caminho {caminho} foi criado com sucesso!')
                return True
    else:
        print(f'Arquivo encontrado {caminho}!')
        return True


def cadastrar(arquivo, pessoa: str):
    with open(arquivo, 'a') as arq:
        arq.write(pessoa)


def listar(arquivo):
    linhas = []
    with open(arquivo, 'rt') as arq:
        arquivo = arq.read().split('\n')
        for i in arquivo:
            linhas.append(i)
        print(f'\033[1;97m{'Nome':<36}{'Idade':<6}\033[m')
        for i in linhas:
            if len(i) != 0:
                pessoa = i.split(';')
                print(f'\033[1;36m{pessoa[0].upper():<36}{pessoa[1].upper():<6}\033[m')
