#PROGRAMA QUE CALCULA O AUMENTO DE 15% NO SALÁRIO DO USUÁRIO.
print('Parabéns! Você foi promovido.')
sal = float(input('Informe o valor atual do seu salário para que o reajuste seja feito. R$'))
novosal = (sal/100) * 115
print('\nO novo valor do seu salário é de R${:.2f}'.format(novosal))