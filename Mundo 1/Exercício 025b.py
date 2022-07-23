# PROGRAMA QUE IDENTIFICA SE O NOME DA PESSOA TEM SILVA OU NÃO.

print('O seu nome tem Silva? True = Sim / False = Não\n')
nome = str(input('Digite o seu nome completo: '))
nome = nome.title()
silva = 'Silva' in nome
# ou print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))
print(silva)


