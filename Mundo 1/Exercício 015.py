#ALUGUEL DE CARROS \\ R$60.00/DIA & R$0.15/KM PERCORRIDO.
print('Calcule quanto você deve pagar pelo carro alugado.')
dia = int(input('Informe quantos dias você ficou com o carro: '))
km = float(input('Informe quantos KM você percorreu com o carro: '))
valor = (dia * 60) + (km * 0.15)
print('\nO valor total do seu aluguel é de R${:.2f}\nTenha um bom dia!'.format(valor))