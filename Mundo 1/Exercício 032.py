#PROGRAMA QUE LÊ O ANO E DIZ SE É BISSEXTO OU NÃO

ano = int(input('Digite um ano para saber se ele é bissexto ou não: '))
div = ano % 4
lista = ['100','200','300','500','600'',700','900','1000','1100','1300','1400','1500','1700','1800','1900']
print('')

if (div == 0):
    print('O ano digitado é bissexto.')

else:
    print('O ano digitado não é bissexto.')