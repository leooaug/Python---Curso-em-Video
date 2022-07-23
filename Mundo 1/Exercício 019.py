# PROGRAMA SORTEIA 1 DE 4 ALUNOS PARA APAGAR O QUADRO.
import random
print('Sorteio para apagar o quadro. Informe o nome de 4 alunos a serem sorteados.')
a1 = str(input('Digite o nome do primeiro aluno: '))
a2 = str(input('Digite o nome do segundo aluno: '))
a3 = str(input('Digite o nome do terceiro aluno: '))
a4 = str(input('Digite o nome do quarto aluno: '))
lista = (a1,a2,a3,a4)
sorteio = random.choice(lista)
print('{} foi o(a) aluno(a) sorteado(a)!'.format(sorteio))