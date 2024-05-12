nomeCity = input('Digite o nome de uma cidade: ')
nomeSplit = nomeCity.split()
print('O nome da cidade {} começa com "Santo"? {}'.format(nomeCity, ('SANTO' in nomeSplit[0].upper())))
