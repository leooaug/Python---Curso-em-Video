#DISSECANDO UMA VARIÁVEL.

c = input('Digite algo: ')
print('Considere True = verdadeiro / False = falso')

print('O valor digitado é numérico? {}'.format(c.isnumeric()))
print('O valor digitado é alfanumérico? {}'.format(c.isalnum()))
print('O valor digitado só tem letras? {}'.format(c.isalpha()))
