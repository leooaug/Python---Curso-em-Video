#NÚMERO PAR OU ÍMPAR.

n = int(input('Digite um número: '))
result = (n % 2)

print('')

if (result == 1):
    print('O número digitado é ímpar.')
else:
    print('O número digitado é par.')