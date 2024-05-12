pessoas = list()
dados = list()
leves = list()
pesadas = list()
quant = med = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    med += dados[len(dados) - 1]
    pessoas.append(dados[:])
    dados.clear()
    quant += 1
    cont = str(input('Deseja continuar? [S/N] '))
    if cont in 'NnnãoNÃO':
        break
med /= quant
for n in range(len(pessoas)):
    if pessoas[n][1] >= med:
        pesadas.append(pessoas[n][0])
    else:
        leves.append(pessoas[n][0])
pesadas.sort()
leves.sort()

print(f'Quantidade de pessoas: {quant}\n'
      f'Mais pesados: {pesadas}\n'
      f'Mais leves: {leves}')
