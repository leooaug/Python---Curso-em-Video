#Programa lê o peso e altura da pessoa, calcula o IMC, e classifica-o nos seguintes status:
#1) Se IMC estiver abaixo de 18.5, "Abaixo do peso".
#2) Se IMC estiver entre 18.5 e 25, "Peso ideal".
#3) Se IMC estiver entre 25 e 30, "Sobrepeso".
#4) Se IMC estiver entre 30 e 40, "Obesidade".
#5) Se IMC estiver acima de 40, "Obesidade mórbida".
#imc = peso(kg) / altura** 2(m)

print('Calcule o seu IMC e veja seu status.\n')

peso = float(input('Digite o seu peso, em KG: '))
altura = float(input('Digite a sua altura, em metros: '))
imc = peso / altura ** 2

if(imc<18.5):
    print('\nO seu IMC é {:.1f} - abaixo do peso.'.format(imc))

elif(18.5<=imc<25):
    print('\nO seu IMC é {:.1f} - peso ideal.'.format(imc))

elif(25<=imc<30):
    print('\nO seu IMC é {:.1f} - Sobrepeso.'.format(imc))

elif(30<=imc<=40):
    print('\nO seu IMC é {:.1f} - Obesidade.'.format(imc))

elif(imc>40):
    print('\nO seu IMC é {:.1f} - Obesidade mórbida.')
