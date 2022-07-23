#Programa que lê duas notas de um aluno, calcula a média, e:
#1) se média < 5 == reprovado / 2) se 5 > média < 6.9 == recuperação / 3) se média > 7 == aprovado

print('Digite suas duas notas para saber se foi reprovado, aprovado, ou se está de recuperação.\n')

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
med = (n1 + n2) / 2

if(med>10):
    print('')
    print('Algum valor foi digitado incorretamente.')

elif(med<5):
    print('')
    print('A média das notas digitadas é {:.2f}.\nVocê foi reprovado!'.format(med))

elif(5<med<6.99):
    print('')
    print('A média das notas digitadas é {:.2f}.\nVocê está de recuperação.'.format(med))

elif(med>7):
    print('')
    print('A média das notas digitadas é {:.2f}.\n\nParabéns!\nVocê foi aprovado!!'.format(med))

