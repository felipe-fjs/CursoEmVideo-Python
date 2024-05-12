saque = total = int(input('Digite o valor a ser sacado: [número inteiro] '))
quant1 = quant10 = quant20 = quant50 = 0
if total >= 50:
    quant50 = total // 50
    total = total % 50
if total >= 20:
    quant20 = total // 20
    total %= 20
if total >= 10:
    quant10 = total // 10
    total %= 10
if total >= 1:
    quant1 = total // 1
print(f'Total: R$ {saque:.2f}\n'
      f'Notas de R$ 50: {quant50}\n'
      f'Notas de R$ 20: {quant20}\n'
      f'Notas de R$ 10: {quant10}\n'
      f'Notas de R$ 1:  {quant1}')
