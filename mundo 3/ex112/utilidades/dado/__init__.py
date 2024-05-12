def leia_dinheiro(msg):
    valido = False
    while not valido:
        msg = str(msg.replace(',', '.')).strip()
        if msg.isalpha() or len(msg) == 0:
            print(f'\033[1;31mERRO! "{msg}" não é um preço válido!\033[m')
        else:
            return float(msg)
        msg = str(input('Digite um valor válida: ')).replace(',', '.')


def leia_taxa(msg):
    valido = False
    while not valido:
        msg = str(msg.replace(',', '.'))
        if msg.isalpha():
            print(f'\033[1;31mERRO! /{msg}/ não é uma taxa válida!\033[m')
        else:
            return float(msg)
        msg = str(input('Digite uma taxa válida: ')).replace(',', '.')
