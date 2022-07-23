#PROGRAMA QUE LÊ 3 NÚMEROS E FALA QUAL É O MAIOR

print('Digite três números para saber qual deles é o maior.')
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))
print('')

if n1 > n2 and n1 > n3:
    print('O número {:.2f} é o maior.'.format(n1))
elif(n2>n1) and n2>n3:
    print('O número {:.2f} é o maior.'.format(n2))
elif(n3 > n1) and n3 > n1:
    print('O número {:.2f} é o maior.'.format(n3))
else:
    print('Você digitou dois ou mais valores iguais.')

