#Programa que lê o comprimento de 3 retas, diz se elas podem formar um triângulo, e classifica-o em:
#1) Equilátero (Todos os lados iguais)
#2) Isósceles (dois lados iguais)
#3) Escaleno (três lados diferentes)
print('Informe o comprimento de três retas para saber qual tipo de triângulo elas formam.\n')

r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))

if r1+r2<r3 or r2+r3<r1 or r1+r3<r2:
    print('')
    print('As retas informadas não podem formar um triângulo.')

elif(r1==r2==r3):
    print('\nAs retas informadas formam um triângulo equilátero.')

elif(r1==r2) or (r1==r3) or (r2==r3):
    print('')
    print('As retas informadas formam um triângulo isósceles.')

else:
    print('')
    print('As retas informadas formam um triângulo escaleno.')
