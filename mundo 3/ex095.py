def mostrarlinha():
    """
     -> Função que faz print de uma linha simples de 60 caracteres na cor branca
    """
    print(f'\033[1;97m{'-' * 60}')


def somalista(* lista):
    soma = 0
    for key in range(len(lista)):
        soma += lista[key]
    print(f'A soma da lista {lista} vale {soma}')


somalista(1, 2, 3, 4)
print(f'\033[1;32m {' Exercicio 095 ':=^60}\033[m')
jogadores = []
jogador = {'nome': str, 'partidas': int, 'golsPartida': list, 'totalGols': int}
cont = totalGols = 0
while True:
    jogador.clear()
    print(f'\033[1;33m{f'{cont + 1}º Jogador':~^60}\033[m ')
    jogador['nome'] = str(input('Nome: '))
    partidas = int(input('Quantidade de partidas: '))
    gols = []
    print(f'{'Quantidade de gols por partida':*^60}')
    for i in range(partidas):
        gols.append(int(input(f'Quantidade de gols part.{i + 1}: ')))
        totalGols += gols[i]
    jogador['golsPartida'] = gols[:]
    jogador['totalGols'] = totalGols
    jogadores.append(jogador.copy())
    cont += 1
    resp = str(input('Deseja continuar? [S/N]')).upper()[0]
    if resp in 'Nn':
        break
print(f'\033[1;32m{'=' * 60}\033[m')
print('\033[1;31mcód. \033[m', end='')
for i in jogador.keys():
    print(f'\033[1;31m{i:<15}\033[m', end='')
print()
for k, v in enumerate(jogadores):
    print(f'\033[1;32m{k:<5}\033[m\033[m', end='')
    for ind in v.values():
        print(f'\033[1;32m{str(ind):<15}\033[m', end='')
    print()

mostrarlinha()
print(f'{'FIM DO PROGRAMA':.^60}')
mostrarlinha()
