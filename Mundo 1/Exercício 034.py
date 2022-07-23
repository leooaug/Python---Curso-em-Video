#DIGITE O SEU SALÁRIO. SE SALÁRIO -> 1250R$, AUMENTO DE 10% // SE SALÁRIO <- 1250R$, AUMENTO DE 15%.

sal = float(input('Você foi promovido! Digite o seu salário para calcularmos seu aumento: '))

if(sal > 1250):
    aum10 = (sal/100) * 110
    print('O seu novo salário é de {:.2f}R$.'.format(aum10))
else:
    aum15 = (sal/100) * 115
    print('O seu novo salário é de {:.2f}R$.'.format(aum15))
