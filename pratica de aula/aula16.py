combo1 = ('Hambuguer', 'Suco', 'Batata frita', 'Pudim')
lista = ['', '', '', '']
for c in range(0, len(combo1)):
    lista[c] = combo1[c]
# 1ª Forma: não dá pra enumerar sem gambiarra
'''for c in combo1:
    print(f'lanche: {c}')'''
# 2ª Forma: o 'c' vai ser o contador para enumerar os itens da tupla
'''for c in range(0, len(combo1)):
    print(f'Lanche {c+1}: {combo1[c]}')'''
# 3ª Forma: são declarados duas variáveis e utilizado a função enumerate()
# 'posi' vai receber a enumeração da posição do item;
# 'lanche' vai receber o item armazenador no indice recebido em posi
'''for lanche, posi in enumerate(combo1):
    print(f'{posi} lanche: {lanche}')'''
print(sorted(lista))


