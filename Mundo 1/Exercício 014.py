#CONVERSOR DE GRAUS CELSIUS PARA FAHRENHEIT. // F = C x 1,8 + 32.
print('Esse é um conversor de graus Celsius para Fahrenheit.')
cels = int(input('Digite os graus Celsius a serem convertidos: '))
fahr = cels * 1.8 + 32
print('{} graus Celsius equivalem a {:.2f} graus Fahrenheit.'.format(cels,fahr))