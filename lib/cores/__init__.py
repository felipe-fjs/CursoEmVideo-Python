def abertura_cor(letra, fundo, estilo=''):
    """
    função desenvolvida para a aplicação de cores apartir do nome delas
    :param letra: recebe o nome da cor que as letras devem receber
    :param fundo: rebebe o nome da cor que o fundo deve receber
    :param estilo: recebe se deve ser bold, underlinede e reversed e pode ficar vazio
    :return: retorna a formação para a aplicação de cor à String
    """
    cor_letra = {'preto': 30, 'vermelho': 31, 'verde': 32, 'amarelo': 33, 'azul': 34, 'magenta': 35, 'ciano': 36,
                 'cinza': 37, 'branco': 97}
    cor_fundo = {'preto': 40, 'vermelho': 41, 'verde': 42, 'amarelo': 43, 'azul': 44, 'magenta': 45, 'ciano': 46,
                 'cinza': 47, 'branco': 107}
    if len(letra) or len(fundo) != 0:
        if len(letra) != 0:
            while letra not in cor_letra:
                letra = str(input(f'Digite um valor válido para a cor da letra: '))
            else:
                letra = cor_letra[letra]
        if len(fundo) != 0:
            while fundo not in cor_fundo:
                fundo = str(input('Digite uma cor válida '
                                  '[preto, vermelho, verde, amarelo, azul, magenta, ciano, cinza, branco]: '))
            else:
                fundo = cor_fundo[fundo]
        if estilo == '':
            cor_retorno = f'\033[{estilo};{letra}m'
        else:
            cor_retorno = f'\033[{estilo};{letra};{fundo}m'
        return cor_retorno


def fechar_cor():
    """
    fecha a aplicação de cores.
    :return:
    """
    return '\033[m'

