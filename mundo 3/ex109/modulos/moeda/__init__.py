def formato(valor=0.0, moeda='R$'):
    return f'{moeda} {valor:.2f}'.replace('.', ',')


def dobro(n=0, forma=False):
    a = 2 * n
    if forma:
        return formato(a)
    else:
        return a


def metade(n=0, forma=False):
    a = n / 2
    if forma:
        return formato(a)
    else:
        return a


def aumentar(n=0, taxa=0, forma=False):
    a = n + (n * taxa/100)
    if forma:
        return formato(a)
    else:
        return a


def diminuir(n=0, taxa=0, forma=False):
    a = n - (n * taxa/100)
    if forma:
        return formato(a)
    else:
        return a


