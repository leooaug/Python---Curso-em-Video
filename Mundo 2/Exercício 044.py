#Programa que calcula o valor de um produto, considerando seu preço normal e forma de pagamento,
#considerando que o pagamento:
#1) à vista: 10% de desconto.
#2) à vista no cartão: 5% de desconto.
#3) 2x no cartão: preço normal.
#4) 3x ou mais no cartão: 20% de juros.

print('Calcule o preço a ser pago no produto.')
preco = float(input('Digite o preço do produto: R$'))
fpag = int(input('Digite o número correspondente à forma de pagamento.\n1) à vista no dinheiro.'
                 '\n2) à vista no cartão.\n3) 2x no cartão.\n4) 3x ou mais no cartão.\n'))

if(fpag==1):

    desconto = (preco/100) * 10
    novovalor = (preco/100) * 90
    print('\nPara a forma de pagamento selecionada, você ganha 10% de desconto.\nO novo valor a ser pago é de {:.2f}R$.'.format(novovalor))

elif(fpag==2):

    novovalor = (preco/100) * 95
    print('\nPara a forma de pagamento selecionada, você ganha 5% de desconto.\nO novo valor a ser pago é de {:.2f}R$.'.format(novovalor))


elif(fpag==3):

    print('\nPara a forma de pagamento selecionada, o valor se mantém inalterado.\nO valor a ser pago é de R${:.2f}'.format(preco))

elif(fpag==4):

    novovalor = (preco/100) * 120
    print('\nPara a forma de pagamento selecionada, o valor terá um acréscimo de 20%.\nO novo valor a ser pago é de R${:.2f}'.format(novovalor))
