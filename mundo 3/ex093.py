print(f'\033[1;32m {' Exercicio 094 ':=^60}\033[m')
print('Digite os dados do Jogador: ')
nome = str(input('Nome: '))
parts = int(input('Quantidade de partidas: '))
gols = []
totalGols = 0
print(f'{'Quantidade de gols por partida':*^60}')
for i in range(parts):
    gols.append(int(input(f'Quantidade de gols part.{i+1}: ')))
    totalGols += gols[i]
jogador = {'nome': nome, 'partidas': parts, 'golspartida': gols, 'totalGols': totalGols}
print(f'\033[1;32m{'FINAL':*^60}\033[m\n'
      f'\033[1;36mNome:\033[m {jogador['nome']}\n'
      f'\033[1;36mPartidas:\033[m {jogador['partidas']}')
for i in range(len(jogador['golspartida'])):
    print(f'    * \033[1;34m{i+1}ª Partida:\033[m {jogador['golspartida'][i]}')
print(f'\033[1;32mTotal Gols:\033[m {jogador['totalGols']}')

