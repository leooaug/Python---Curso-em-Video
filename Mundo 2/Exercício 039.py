#Programa que lê a idade de um jovem, e diz se:
#1) Ainda não é hora de se alistar. /
# 2) Está na hora de se alistar. /
# 3) Se já passou do prazo de alistamento.
#Quanto tempo já passou ou quanto tempo ainda falta para o alistamento? O programa deve mostrar.

print('Está na hora de se alistar ao serviço militar? Consulte.\n')

idade = int(input('Digite sua idade: '))

if(idade<18) and (idade!=17):
    idade = 18 - idade
    print('Ainda faltam {} anos para você se alistar.'.format(idade))

elif(idade==17):
    print('Ainda falta 1 ano para você se alistar.')

elif(idade==18):
    print('Está na hora de se alistar!')

elif(idade>18):
    idade = idade - 18
    print('Sua idade excede o prazo do alistamento. Você devia ter se alistado há {} anos.'.format(idade))
