#DIGITE UM NÚMERO PARA SABER SUA CARREIRA DAS UNIDADES, DEZENAS, CENTENAS E MILHARES

n1 = str(input('Digite um número de 1000 a 9999: '))

div = n1.split()
print(div[0][0],'= milhares\n', div[0][1], '= centenas\n', div[0][2], '= dezenas\n', div[0][3], '= unidades')

#TRATEI O NÚMERO COMO STRING!!