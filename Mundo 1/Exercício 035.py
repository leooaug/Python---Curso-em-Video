#PROGRAMA QUE LÊ O COMPRIMENTO DE 3 RETAS E DIZ SE ELAS PODEM OU NÃO FORMAR UM TRIÂNGULO.

print('Digite a medida de 3 retas para saber se elas podem ou não formar um triângulo.')
r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))
print('')

if r3 + r2 > r1 and r1 + r2 > r3 and r1 + r3 > r2:
    print('As medidas informadas podem formar um triângulo.')

else:
    print('As medidas informadas não podem formar um triângulo.')
