def dobro(n=0):
    a = 2 * n
    return a


def metade(n=0):
    a = n / 2
    return a


def aumentar(n=0, taxa=0):
    a = n + (n * taxa/100)
    return a


def diminuir(n=0, taxa=0):
    a = n - (n * taxa/100)
    return a


def formato(valor=0, moeda='R$'):
    return f'{moeda} {valor:.2f}'.replace('.', ',')

