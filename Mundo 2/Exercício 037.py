#PROG LÊ UM NÚMERO INTEIRO E DÁ OPÇÃO DE ESCOLHA DE CONVERSÃO DO NÚMERO.
#1) BINÁRIO / 2) OCTAL / 3) HEXADECIMAL

print('Converta seu número para binário, octal ou hexadecimal.')

n1 = int(input('Digite o número a ser convertido: '))
n2 = int(input('Digite 1 para conversão em binário, 2 para octal e 3 para hexadecimal: '))

if(n2==1):
    print('O número digitado em binário é {}'.format(bin(n1)[2:]))

elif(n2==2):
    print('O número digitado em formato octal é {}'.format(oct(n1)[2:]))

elif(n2==3):
    print('O número digitado em format hexadecimal é {}'.format(hex(n1)[2:]))

else:
    print('O valor digitado não é válido.')