# PROGRAMA LÊ O CATETO OPOSTO E ADJACENTE DE UM NÚMERO E MOSTRA NA TELA SUA HIPOTENUSA.
# a² = b² + c²
print('Calcule a hipotenusa de um triângulo informando seu cateto oposto e adjacente.\n')
catop = float(input('Digite o comprimento do cateto oposto do triângulo retângulo: '))
catadj = float(input('Digite o comprimento do cateto adjacente do triângulo retângulo: '))
fhip = (catop**2) + (catadj**2)
hip = pow(fhip,(1/2))
print('A hipotenusa para as medidas informadas é {:.2f}'.format(hip))
