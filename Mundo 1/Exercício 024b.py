#a cidade começa com a palavra santo ou não?
print('O nome da sua cidade começa com a palavra Santo? (True = Sim / False = Não)')
print('')
cidade = str(input('Digite o nome da sua cidade: '))

cidade = cidade.title()
cidade = cidade.strip()

corte = len(cidade) - cidade.count(' ')

c = cidade[:5] == 'Santo'
print(c)
