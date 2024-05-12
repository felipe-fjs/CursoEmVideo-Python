def formato(valor=0.0, moeda='R$'):
    return f'{moeda} {valor:>.2f}'.replace('.', ',')


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


def resumo(n=0, taxaup=0, taxadown=0):
    print(f'\033[1;97m{'-'*(len('resumo')+36)}\n'
          f'{' '*18}Resumo \n'
          f'{'-'*(len('resumo')+36)}\033[m')
    print(f'{'Valor analisado:':<30}{formato(n):>8}')
    print(f'{'Dobro de ' + formato(n) + ':':<30}{formato(dobro(n)):>8}\n'
          f'{'Metade de ' + formato(n) + ':':<30}{formato(metade(n)):>8}\n'
          f'{'Aumento de ' + str(taxaup) + '%:':<30}{formato(aumentar(n, taxaup)):>8}\n'
          f'{'Diminuição de ' + str(taxadown) + '%:':<30}{diminuir(n, taxadown, True):>8}')
    return ''
