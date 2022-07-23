#PROGRAMA LÊ UM VALOR E CALCULA 5% DE DESCONTO.
print('Você ganhou um desconto de 5%!')
preco = float(input('Informe o valor original do produto: R$'))
desc = (preco/100) * 95
print('O novo valor do produto é de R${}'.format(desc))