from datetime import datetime


def linha(frase):
    print('~'*(len(frase)+6))
    print(f'  {frase}')
    print('~'*(len(frase)+6))


def voto(nascimento):
    """
    :param nascimento: recebe o ano de nascimento da pessoa em forma de um número inteiro
    :return: retorna se a pessoa tem voto obrigatório, opcional ou não pode votar
    """
    idade = datetime.today().year - nascimento
    if 16 > idade:
        result = f'Você tem {idade} anos. NÃO PODE VOTAR!'
    elif idade < 18 or idade > 60:
        result = f'Você tem {idade} anos, possuindo voto opcional!'
    else:
        result = f'Você tem {idade} anos, possuindo VOTO OBRIGATÓRIO!'
    return result


linha('Exercício 101')
nasci = int(input(f'Ano de nascimento: '))
print(voto(nasci))
