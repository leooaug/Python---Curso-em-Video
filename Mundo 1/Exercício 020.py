#PROGRAMA QUE SORTEIA A ORDEM DOS 4 ALUNOS.
import random
print('Sorteio para apagar parte do quadro. Digite o nome de 4 alunos e saiba quem vai apagar qual parte.')
a1 = str(input('Digite o nome do(a) primeiro(a) aluno(a): '))
a2 = str(input('Digite o nome do(a) segundo(a) aluno(a): '))
a3 = str(input('Digite o nome do(a) terceiro(a) aluno(a): '))
a4 = str(input('Digite o nome do(a) quarto(a) aluno(a): '))

lista = [a1,a2,a3,a4]
random.shuffle(lista)
#random.shuffle não pode ser atribuído à variáveis!! Ele só embaralha.
print(random.shuffle(lista))
print('A ordem dos nomes sorteados foi {}'.format(lista))
