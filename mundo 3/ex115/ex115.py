from lib.interface import *
from lib.arquivo import *
from time import sleep
try:
    # Recebendo caminho de arquivo e verificando se existe,
    # se não existir, será perguntado se quer criar um com esse nome.
    caminho = str(input('Nome do arquivo: '))
    arq = arquivo_existe(caminho)
    if arq:
        while True:
            cabeçalho('MENU PRINCIPAL')
            op = menu(['Cadastrar', 'Listar cadastrados', 'Sair do sistema'])
            if op == 1:
                cabeçalho('Cadastro')
                nome = str(input('Digite seu nome: '))
                idade = str(ler_inteiro(input('Digite sua idade: ')))
                cadastrar(caminho, f'{nome};{idade}\n')
            elif op == 2:
                cabeçalho('Lista')
                listar(caminho)
            elif op == 3:
                cabeçalho('SAINDO DO PROGRAMA... Volte logo!')
                break
            sleep(1.5)
    else:
        cabeçalho('\033[1;31mHOUVE ALGUM ERRO NA CRIAÇÃO DO ARQUIVO!\n'
                  'SAINDO DO PROGRAMA!')
except KeyboardInterrupt:
    print()
    cabeçalho('O programa foi encerrado pelo usuário!')
