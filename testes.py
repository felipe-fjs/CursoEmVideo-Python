def soma(s: str) -> int:
    valores = []
    sum = 0
    for i in s:
        valores.append(ord(i))
    for i in range(len(valores)-1, 0, -1):
        valor = valores[i] - valores[i - 1]
        if valor < 0:
            sum += - valor
        else:
            sum += valor
    return sum


print(soma('hello'))
