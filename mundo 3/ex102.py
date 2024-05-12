def linha(frase):
    print('~'*(len(frase)+40))
    print(f'{' '*20}{frase}{' '*20}')
    print('~'*(len(frase)+40))


def fatorial(num, show=True):
    """-> Função que calcúla o fatoria de um número 'num'
    :param num: Recebe o número que será feito fatorial;
    :param show: determina se será mostrada a operação fatorial
    :return: possui retorno do valor final do fatorial
    """
    fat = 1
    if show:
        for key in range(num, 0, -1):
            fat *= key
            if key == 1:
                print(f'{key}', end=' = ')
                print(f'{fat}')
            else:
                print(f'{key}', end=' x ')
        return fat
    else:
        for key in range(num, 0, -1):
            fat *= key
        return fat


linha('Exercicio 102')
n = int(input(f'Digite o número que será feito fatorial: '))
fatorial(n)     
