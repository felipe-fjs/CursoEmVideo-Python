print(f'\033[1;31m{'='*20} Exericicio 089 {'='*20}\033[m')
alunos = []
dados = []
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Nota 1: ')))
    dados.append(float(input('Nota 2: ')))
    dados.append((dados[1]+dados[2])/2)
    alunos.append(dados[:])
    dados.clear()
    cont = str(input('Deseja continuar? [S/N]'))
    if cont in 'NnNãonãoNÃO':
        break
for c in range(len(alunos)):
    print(f'\033[1;32mALUNO: {alunos[c][0][0:7]}\033[m\n'
          f'    \033[1;31mNOTA 1: \033[m{alunos[c][1]}\n'
          f'    \033[1;31mNOTA 2: \033[m{alunos[c][2]}\n'
          f'    \033[1;31mMÉDIA FINAL: \033[m{alunos[c][3]:.2f}')
