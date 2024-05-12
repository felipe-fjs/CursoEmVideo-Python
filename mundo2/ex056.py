quantF = 0
nomeMaisVelho = ''
idadeMaisVElho = 0
idade = 0
idadeAnt = 0
mediaIdade = 0
sexo = ''
for c in range(0, 4):
    print('------- {}ª Pessoa: --------'.format(c+1))
    nome = input('Nome: ')
    idadeAt = int(input('Idade: \033[[1;32m'))
    sexo = input('Digite seu sexo (M ou F): ').upper()
    idade += idadeAt
    if sexo == 'M':
        if idadeAt > idadeAnt:
            nomeMaisVelho = nome
            idadeMaisVElho = idadeAt
    else:
        if idadeAnt < 20:
            quantF += 1
    idadeAnt = idadeAt

mediaIdade = idade/4
print('Média de idade: {}\n'
      'O homem mais velho tem {} e se chama {}\n'
      'Quantidade de mulheres menor de 20 anos: {}'.format(mediaIdade, idadeMaisVElho, nomeMaisVelho, quantF))
