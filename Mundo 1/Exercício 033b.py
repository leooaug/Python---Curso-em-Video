# MENOR E MAIOR VALOR DIGITADO

print('Digite três valores para saber qual deles é o menor.')
print('')

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))

maior = 0
menor = 0

if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

if n1 < n2 and n1 < n3:
    menor = n1
elif n2 < n1 and n2 < n3:
    menor = n2
elif n3 < n1 and n3 < n2:
    menor = n3

print('O menor número digitado é {:.2f}'.format(menor))
print('O maior valor digitado é {:.2f}'.format(maior))
