km = int(input('Digite a distância a ser percorrida em KM: '))
if km <= 200:
    preco = km*0.5
else:
    preco = km*0.45
print('O valor cobrado para a viagem de {} Kms é de R$ {:.2f}'.format(km, preco))
