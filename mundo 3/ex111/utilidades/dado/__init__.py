def leia_dinheiro(msg):
    valido = False
    while not valido:
        msg = str(input(msg))
        if msg.isalnum():
            print(f'ERRO! {msg} não é um preço válido!')
        else:
            return float(msg)
