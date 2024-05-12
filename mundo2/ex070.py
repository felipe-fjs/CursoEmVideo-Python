quant = nMaisMil = soma = maisBarato = 0

while True:
    quant += 1
    print(f'\033[1;32;40m{'='*16} {quant}º PRODUTO {'='*16}\033[m')
    nome = str(input('\033[1;33mNome do produto:\033[m '))
    preco = float(input('\033[1;33mPreço do produto:\033[m '))
    if quant == 1 or maisBarato > preco:
        maisBarato = preco
        nomeMais = nome
    if preco > 1000:
        nMaisMil += 1

    soma += preco
    cont = str(input('Deseja continuar? [N/S]'))
    while cont.upper() not in 'SN':
        cont = str(input('Deseja continuar? [N/S]'))
    if cont.upper() == 'N':
        break
print(f'\033[1;32m{'='*40}\033[m\n'
      f'TOTAL DA COMPRA:                 R$ {soma:.2f}\n'
      f'PRODUTOS MAIS DE R$ 1000.00:           {nMaisMil}\n'
      f'MAIS BARATO:  {nomeMais:^}  R$ {maisBarato:.2f}')
print(f'{'FIM DO PROGRAMA':-^40}')
