def fatorial(num=1):
    fat = 1
    for key in range(num, 0, -1):
        fat *= key
    return fat


print(fatorial(5))

"""def fraselinhas(frase: str):
    print(f'{'~'*60}')
    print(f'{frase.upper():^60}')
    print(f'{'~'*60}')


def dobrarlista(lista):
    lista1 = lista[:]
    for key in range(len(lista1)):
        lista1[key] *= 2
    print(lista1)


#  programa principal
nums = []
for i in range(5):
    n = int(input(f'{i+1}º número: '))
    if i == 0:
        nums.append(n)
    else:
        for c in range(len(nums)):
            if nums[c] > n:
                nums.insert(c, n)
                break
        if i == len(nums):
            nums.append(n)
print(nums)
dobrarlista(nums)
print(nums)"""

"""print(f'\033[1;31m{'='*20} Exericicio 089 {'='*20}\033[m')
alunos = []
dados = []
while True:
    dados.append(str(input('Nome: ')))
    alunos.append(dados[:])
    dados.clear()
    dados.append(float(input('Nota 1: ')))
    dados.append(float(input('Nota 2: ')))
    dados.append((dados[0]+dados[1])/2)
    alunos[len(alunos)-1].append(dados[:])
    dados.clear()
    cont = str(input('Deseja continuar? [S/N]'))
    if cont in 'NnNãonãoNÃO':
        break
for c in range(len(alunos)):
    print(f'\033[1;32mALUNO: {alunos[c][0][0:7]}\033[m\n'
          f'    \033[1;31mNOTA 1: \033[m{alunos[c][1][0]}\n'
          f'    \033[1;31mNOTA 2: \033[m{alunos[c][1][1]}\n'
          f'    \033[1;31mMÉDIA FINAL: \033[m{alunos[c][1][2]:.2f}')   """

"""aluno = dict()
alunos = list()

while True:
    aluno['nome'] = str(input('Nome do aluno: '))
    aluno['nota1'] = float(input('Nota 1: '))
    aluno['nota2'] = float(input('Nota 2: '))
    aluno['media'] = (aluno['nota1'] + aluno['nota2'])/2
    alunos.append(aluno.copy())
    cont = str(input('Quer continuar? [S/N] '))
    if cont in 'NnNÃOnão':
        break
for al in alunos:
    print(f'{al['nome']}:\n'
          f'    * Nota 1: {al['nota1']}\n'
          f'    * Nota 2: {al['nota2']}\n'
          f'    * MÉDIA : {al['media']:.2f}')"""

print(f'\033[1;32m {' Exercicio 095 ':=^60}\033[m')
jogadores = []
jogador = {'nome': str, 'golspartida': list, 'totalGols': int}
while True:
    print('Digite os dados do Jogador: ')
    jogador['nome'] = str(input('Nome: '))
    partidas = int(input('Quantidade de partidas: '))
    gols = []
    totalGols = 0
    print(f'{'Quantidade de gols por partida':*^60}')
    for i in range(partidas):
        gols.append(int(input(f'Quantidade de gols part.{i + 1}: ')))
        totalGols += gols[i]
    jogador['golspartida'] = gols[:]
    jogador['totalGols'] = totalGols
    jogadores.append(jogador.copy())
    jogador.clear()
    cont = str(input('Deseja continuar? [S/N]'))
    if cont in 'NnNÃOnão':
        break

print(f'\033[1;32m{'FINAL':*^60}\033[m')
print(f'{'cod.':<5}{'NOME':<15}{'GOLS':<15}{'TOTAL':<5}')
for k, v in enumerate(jogadores):
    print(f'{k:<5}', end='')
    for ind in v.values():
        print(f'{str(ind):<15}', end='')
    print()
print(f'{'FIM DO PROGRAMA':.^60}')
