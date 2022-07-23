#PROGRAMA QUE LÊ O NOME COMPLETO DA PESSOA, MAS SÓ MOSTRA O PRIMEIRO E O ÚLTIMO NA TELA.

nome = str(input('Digite o seu nome completo: '))
nome = nome.strip()
n1 = nome.split()

print('É um prazer te conhecer,',n1[0], n1[-1])
