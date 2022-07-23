#PROGRAMA LÊ A VELOCIDADE DO CARRO. QUANDO ACIMA DE 80KM, PAGA R$7.00 DE MULTA PARA CADA KM ACIMA DO LIMITE.

print('CÁLCULO DE MULTAS COM BASE NA VELOCIDADE DO CARRO.')
m = int(input('Qual era a velocidade do carro, em km/h, no momento em que passou pelo radar? '))
multa = (m - 80) * 7
if(m>80):
    print('Sua velocidade ultrapassou o limite permitido! Pague R${:.2f} de multa no DETRAN.'.format(multa))
else:
    print('Sua velocidade obedece o limite permitido. Você está isento de multas.')