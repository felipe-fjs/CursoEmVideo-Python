def linha(frase):
    print('~'*(len(frase)+40))
    print(f'{' '*20}{frase}')
    print('~'*(len(frase)+40))


def notas(nota: list, situacao=True):
    """->Função calcula a média das notas passadas e sua situação
    :param nota: Recebe uma lista de notas
    :param situacao: Informa qual a situação da turma (ruim, razoável ou boa) a depender da média
    :return: retorna um dicionário contendo total de notas, maior e menor nota, média e situação
    """
    s = 0
    for key in range(len(nota)):
        s += nota[key]
    media = s / len(nota)
    if situacao:
        if media < 6:
            situacao = 'RUIM'
        elif media < 7:
            situacao = 'razoável'.upper()
        else:
            situacao = 'boa'.upper()
    tur = {'total': len(nota), 'maior': max(nota), 'menor': min(nota),
             'media': media, 'situacao': situacao}
    return tur


linha('Exercicio 105')
quant = int(input('Quantas notas serão informadas? '))
notas1 = []
for i in range(quant):
    notas1.append(float(input(f'{i+1}ª Nota: ')))
turma = notas(notas1)
print(f'Total de notas: {turma['total']}\n'
      f'Maior: {turma['maior']}\n'
      f'Menor: {turma['menor']}\n'
      f'Média: {turma['media']:.2f}\n'
      f'Situação: {turma['situacao']}')
