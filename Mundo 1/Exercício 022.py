#O USUÁRIO DIGITA O NOME, APARECE O NOME
# 1) COM TODAS AS LETRAS MAIÚSCULAS;
# 2) COM TODAS AS LETRAS MINÚSCULAS;
# 3) QUANTAS LETRAS TEM AO TOTAL (SEM CONSIDERAR ESPAÇOS);
# 4) QUANTAS LETRAS TEM O PRIMEIRO NOME;

nome = str(input('\033[1;31;40mDigite o seu nome:\033[m '))
# 1 & 2
print('\033[0;35mSeu nome em letras maiúsculas é\033[m ',nome.upper())
print('\033[0;37mSeu nome em letras minúsculas é\033[m ',nome.lower())

#espaco = nome.strip()
#print(len(espaco))

#3)
div = nome.strip()
a5 = len(div) - nome.count(' ')

print('\033[0;32mO nome digitado tem {} letras.\033[m'.format(a5))

#4)
divisao = nome.split()
cont = len(divisao[0])
print('\033[0;34mO nome digitado tem {} letras no primeiro nome.\033[m'.format(cont))

#PARA O 3, SUBTRAÍ A QUANTIDADE DE ESPAÇOS QUE O MEIO DAS PALAVRAS TINHAM. (VI NO VÍDEO)