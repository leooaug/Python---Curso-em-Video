#Programa lê dois números inteiros, e mostra na tela qual valor é maior, ou se os valores são iguais.

print('Digite dois números para saber qual deles é o maior.')
print('')
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))

if(n1>n2):
    print('O número {:.2f} é o maior.'.format(n1))
elif(n2>n1):
    print('O número {:.2f} é o maior.'.format(n2))
elif(n1==n2):
    print('Os dois números têm o mesmo valor.')
