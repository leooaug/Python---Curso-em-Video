#PROGRAMA QUE LÊ UM NÚMERO FLOAT E MOSTRA NA TELA A PARTE INTEIRA
num = float(input('Digite um número qualquer e saiba sua porção inteira: '))
print('A porção inteira do número digitado é {}.'.format(num.__int__()))