print(f'\033[1;33m{' Exercicio 090 ':=^60}\033[m')
aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['nota1'] = float(input('Nota 1: '))
aluno['nota2'] = float(input('Nota 2: '))
aluno['media'] = (aluno['nota1'] + aluno['nota2']) / 2
aluno['situacao'] = 'APROVADO' if aluno['media'] >= 7 else 'REPROVADO'

print(f'Aluno {aluno['nome']}\n'
      f'    * Nota 1: {aluno['nota1']}\n'
      f'    * Nota 2: {aluno['nota2']}\n'
      f'    * Média: {aluno['media']:.2f}\n'
      f'    * Situação: {aluno['situacao']}')
