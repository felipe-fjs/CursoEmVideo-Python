def linha():
    print(f'\033[1;97m{'-'*40}\033[m')


def arearet(larg, comp: float):
    area = larg * comp
    print(f'A área do retangulo {larg}x{comp} é {area:.2f} m2')
    return area


def entrelinhas(frase: str):
    print(f'\033[1;97m{'-'*40}\033[m')
    print(f'{frase.upper():^40}')
    print(f'\033[1;97m{'-'*40}\033[m')


entrelinhas('calcular área')
largu = float(input(f'Largura (m): '))
compri = float(input(f'Comprimento (m): '))
area = arearet(largu, compri)
linha()
