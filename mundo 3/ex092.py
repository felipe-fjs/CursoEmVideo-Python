import datetime
print(f'\033[1;32m{' Exercicio 092 ':=^60}\033[m')
ctps = {'nome': str(input('Nome: ')), 'idade': datetime.datetime.today().year - int(input('Ano de nascimento: ')),
        'carteira': int(input('Nº CTPS [0 se não possuir]'))}
print(f'{'='*60}')
if ctps['carteira'] != 0:
    ctps['anoContrat'] = int(input('Digite o ano de contratação: '))
    ctps['sal'] = float(input('Digite seu salário: '))
    ctps['aposent'] = ctps['idade'] + (35 - (datetime.datetime.today().year - ctps['anoContrat']))
print('='*60)
print(f'\033[1;33mNome:\033[m {ctps['nome']}\n'
      f'\033[1;33midade:\033[m {ctps['idade']}\n'
      f'\033[1;33mCTPS:\033[m {ctps['carteira']}', end='')

if ctps['carteira'] != 0:
    print(f'\033[1;33mAno contratação:\033[m {ctps['anoContrat']}\n'
          f'\033[1;33mSalário:\033[m {ctps['sal']}\n'
          f'\033[1;33mIdade para aposentadoria:\033[m {ctps['aposent']}')
