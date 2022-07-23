#Programa que lê o ano de nascimento de um atleta e mostra a sua classificação de acordo com a idade.
#Até 9 anos == mirim
#Até 14 anos == infantil
#Até 19 anos == Júnior
#Até 20 anos == Sênior
#Acima de 20 anos == Master
print('Informe seu ano de nascimento para saber sua classificação na natação.\n')

ano = int(input('Digite o ano em que você nasceu: '))
idade = 2022 - ano

if(idade>100):
    print('')
    print('Você não está apto para competir.')

elif(idade<=9):
    print('')
    print('Sua classificação é de atleta mirim.')

elif(10<=idade<=14):
    print('')
    print('Sua classificação é de atleta infantil.')

elif(15<=idade<=19):
    print('')
    print('Sua classificação é de atleta júnior.')

elif(idade==20):
    print('')
    print('Sua classificação é de atleta sênior.')
elif(idade>20):
    print('')
    print('Sua classificação é de atleta master.')
