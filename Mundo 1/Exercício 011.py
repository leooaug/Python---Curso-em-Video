#PROGRAMA LÊ A ALTURA E LARGURA DE UMA PAREDE, EM M, FALA A ÁREA E QUANTOS L DE TINTA P/ PINTÁ-LA. 1L = 2M²
print('Informe a altura e a largura de uma parede. O programa calculará a área e quantos litros de tinta'
      'serão gastos para pintá-la por completo.')
alt = float(input('Altura: '))
larg = float(input('Largura: '))
area = alt * larg
ltinta = area/2
print('Para pintar essa parede, de área {:.2f}m², serão gastos {:.2f}L de tinta.'.format(area,ltinta))