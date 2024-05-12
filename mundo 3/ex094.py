print(f'\033[1;33m{' Exercicio 094 ':~^60}\033[m')
pessoa = {'nome': str, 'sexo': str, 'idade': int}
pessoas = [[], [], []]
# 1ª lista: todos dicionários; 2ª lista: somente mulheres; 3ª lista: pesoas com idade acima da média
quant = media = 0
while True:
    print(f'* {quant + 1}ª Pessoa: ')
    pessoa['nome'] = str(input('    * Nome: '))
    pessoa['sexo'] = str(input('    * Sexo [M/F]:').upper())
    idade = int(input('   * Idade: '))
    pessoa['idade'] = idade
    media += idade
    pessoas[0].append(pessoa.copy())
    if pessoa['sexo'] in 'fF':
        pessoas[1].append(pessoa.copy())
    pessoa.clear()
    quant += 1
    cont = str(input('Deseja continuar? [S/N]'))
    if cont in 'NnNÃOnão':
        break
media /= quant
for i in range(len(pessoas[0])):  # para add a lista acima da média
    if pessoas[0][i]['idade'] > media:
        pessoas[2].append(pessoas[0][i].copy())
print(f'Quantidade de pessoas: {len(pessoas[1])}\n'
      f'Média de idade: {media:.2f}\n'
      f'\033[1;31mMulheres:\033[m ', end='')
if len(pessoas[1]) > 0:  # mostrar mulheres (lista[1])
    print()
    for i in range(len(pessoas[1])):
        print(f'    \033[1;31m* {i+1}ª Mulher:\033[m\n'
              f'        \033[31m* Nome: {pessoas[1][i]['nome']}\n'
              f'        * Idade: {pessoas[1][i]['idade']}\033[m')
else:
    print('Nenhuma mulher foi cadastrada!')
print(f'\033[1;34mPessoas com idade acima da média: \033[m')
for i in range(len(pessoas[2])):
    print(f'    \033[1;34m {i+1}ª Pessoas:\033[m \n'
          f'        \033[34m* Nome: {pessoas[2][i]['nome']}\n'
          f'        * Sexo: {pessoas[2][i]['sexo']}\n'
          f'        * Idade: {pessoas[2][i]['idade']}\033[m')
print(f'\033[1;33m{'Fim do programa':=^60}\033[m')
