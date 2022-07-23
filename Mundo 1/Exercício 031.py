#DIGITE A DISTÂNCIA DA VIAGEM EM KM, 0,50r$ POR KM PARA VIAGENS ATE 200 KM
# 0,45R$ POR KM SE MAIS DE 200KM RODADOS

print('Cálculo do preço da sau viagem.')
print('')
km = float(input('Digite quantos quilômetros você pretende rodar: '))

if (km >= 200):
    km201 = km * 0.45
    print('Para rodar {:.0f}km, você pagará {:.2f}R$.'.format(km, km201))
else:
    km199 = km * 0.50
    print('Para rodar {:.0f}km, você pagará {:.2f}R$.'.format(km, km199))
