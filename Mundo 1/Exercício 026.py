#PROGRAMA QUE LÊ UMA FRASE E MOSTRA
# 1) QUANTAS LETRAS 'A' A FRASE TEM.
# 2) A POSIÇÃO DA PRIMEIRA LETRA 'A'
# 3) A POSIÇÃO DA ÚLTIMA LETRA 'A'

frase = str(input('Digite uma frase qualquer: '))
frase = frase.strip()
ndeamin = frase.count('a')
ndeamaiusc = frase.count('A')
ndea = ndeamin + ndeamaiusc
print('\nA frase digitada tem {} letras "a".'.format(ndea))
print('')
a1 = frase.find('a')
print('A primeira letra "a" da frase se encontra na posição {}.'.format(a1))
a2 = frase.rfind('a')
print('A última letra "a" da frase se encontra na posição {}.'.format(a2))