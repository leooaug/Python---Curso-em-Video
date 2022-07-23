#PROGRAMA LÊ O NOME DA CIDADE E DIZ SE COMEÇA OU NÃO COM 'SANTO'

print('Se o retorno do programa for 0, o nome da cidade digitada começa com a palavra "Santo".')
print('Caso contrário, o nome da cidade começa com outro nome.')
print('')

c = str(input('Digite o nome da sua cidade: '))
c1 = c.find('Santo')
c2 = c.title()
#santo = c.find(s1)
#santo1 = c.find(s2)
#santo2 = c.find(s3)
print('Começa com a palavra "Santo?" ', c2.find('Santo'))
