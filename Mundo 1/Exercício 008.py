# PROGRAMA LÊ UM VALOR EM METROS E O CONVERTE PARA CENTÍMETROS E MILÍMETROS.
met = float(input('Digite um valor em metros e o tenha convertido em centímetros e milímetros: '))
cm = met/100
mm = met/1000
print('{:.2f}m = {:.2f}cm'.format(met,cm))
print('{:.2f}m = {:.2f}mm'.format(met,mm))