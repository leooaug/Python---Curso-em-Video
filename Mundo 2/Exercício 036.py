#PROGRAMA PARA APROVAR O EMPRÉSTIMO BANCÁRIO PARA A COMPRA DE UMA CASA.
#PERGUNTE O VALOR DA CASA, O SALÁRIO DO COMPRADOR E EM QUANTOS ANOS VAI PAGAR.
#CALCULE O VALOR DA PRESTAÇÃO MENSAL. SE PREST > 30% SALARIO == NEGADO

print('Consulte o status do seu empréstimo para financiar um imóvel.')
vimovel = int(input('Digite o valor do imóvel: R$'))
salario = float(input('Digite o valor do seu salário: R$'))
anos = int(input('Em quantos anos deseja pagar a casa? '))

meses = anos * 12
prest = vimovel / meses
limite = (salario/100) * 30
print('')

if (prest>limite):
    print('O seu financiamento foi negado.\nPara pagar a casa em {} ano(s), '
          'as prestações seriam de {}R$, valor que excede 30% do seu salário.'.format(anos, prest[2:]))

elif(prest<=limite):
    print('O seu financiamento foi aprovado!')
    print('O valor das prestações será de R${:.2f}.'.format(prest))

#DONE