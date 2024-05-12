print(f'\033[1;32;40m {'='*15} Exercicio 069 {'='*15} \033[m')
quant = men = women20 = people18 = 0

while True:
    quant += 1
    print(f'{'~'*15} {quant}ª pessoa {'~'*15}')
    idade = int(input('Digite sua idade: '))

    while idade != int or idade <= 0 or idade is None:
        idade = int(input('Digite sua idade [DIGITE UM NÚMERO INTEIRO E POSITIVO]: '))
    sexo = str(input('Digite seu sexo [M/F]: '))
    while sexo.upper() not in ['M', 'F']:
        sexo = str(input('Digite seu sexo [M/F] [DIGITE SOMENTE M PARA MASCULINO E F PARA FEMININO: '))

    if idade > 18:
        people18 += 1
    if idade < 20 and sexo.upper() in 'F':
        women20 += 1
    if sexo.upper() == 'M':
        men += 1
    cont = str(input('Deseja continuar? [S/N] '))
    while cont.upper() not in ['S', 'N']:
        cont = str(input('DIGITE \033[1;32mS\033[m PARA CONTINUAR OU \033[1;31mN\033[M PARA PARAR: '))
    if cont.upper() in ['N', 'NAO', 'NÃO']:
        print(f'{'~' * 40}')
        break

print(f'\033[1;32mPessoas com mais de 18 anos\033[m: {people18}\n'
      f'\033[1;32mHomens cadastrados\033[m: {men}\n'
      f'\033[1;32mMulheres com menos de 20 anos\033[m: {women20}')
print(f'\033[1;31m {'-='*16} FIM DO PROGRAMA {'=-'*16}\033[m')
