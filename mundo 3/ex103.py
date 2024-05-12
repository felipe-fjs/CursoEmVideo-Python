def linha(frase: str):
    print('~'*(len(frase)+20))
    print(f'{' '*10}{frase}')
    print('~'*(len(frase)+20))


def fimlinha(exercicio):
    print(f'{'Fim do Exericicio ' + exercicio:~^40}')


def ficha_jogador(nome='<Desconhecido>', gols=0):
    if nome == '':
        nome = '<Desconhecido>'
    print(f'O jogador {nome} realizou {gols} gol(s) no campeonato')


linha('Exercicio 103')
name = str(input('Nome do jogador: '))
gol = str(input('Gols marcados: '))
if gol == '':
    gol = 0
else:
    gol = int(gol)

ficha_jogador(name, gol)
fimlinha('103')
