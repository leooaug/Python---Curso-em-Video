#PROGRAMA QUE FAZ O COMPUTADOR PENSAR EM UM NÚMERO DE 1 A 5, E ESCREVE SE O USUÁRIO ACERTOU OU ERROU.

import random

lista = ('1', '2', '3', '4', '5')
print('Tente adivinhar o número escolhido pelo computador.')
n1 = random.choice(lista)
n = str(input('Digite um número de 1 a 5: '))

if (n1 == n):
    print('Parabéns! Você acertou o número escolhido pelo programa.')
else:
    print('Errou! O número escolhido pelo computador foi {}!'.format(n1))
