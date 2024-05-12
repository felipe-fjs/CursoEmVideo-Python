def soma(a=0, b=0, c=1):
    s = a + b + c
    print(f'a soma dos valores vale {s}')


def linhavaria(frase: str):
    """

    :param frase: recebe uma String que será impressa entre as linhas, que variarão conforme o
    tamalho da String.
    :return: sem retorno
    """
    tam = len(frase)
    print(f'{'~'*(tam+6)}\n'
          f'{' '*3}{frase}{' '*3}\n'
          f'{'~'*(tam+6)}')


soma()
help(linhavaria)
linhavaria('ola')
linhavaria('Felipe Joaquim')
