# programa que faz o computador jogar JOKENPÔ com o usuário.
import time
import random

print('JOKENPÔ')
escolha = str(input('Escolha entre \033[1;37m"pedra"\033[m, \033[1;36m"papel"\033[m ou '
                    '\033[1;31m"tesoura"\033[m: '))

lista = ['pedra','papel','tesoura']
rnd = random.choice(lista)
escolha = escolha.lower()
time.sleep(1)
print('JO...')
time.sleep(1)
print('KEN...')
time.sleep(1)
print('PÔ!!!')
time.sleep(0.5)

#grupo usuário pedra
if(escolha == 'pedra' and rnd == 'papel'):
    print('Você \033[1;31mperdeu!\033[m O computador escolheu papel!')
elif(escolha=='pedra' and rnd =='pedra'):
    print('Vocês \033[1;33mempataram!\033[m Ambos escolheram pedra.')
elif(escolha=='pedra' and rnd =='tesoura'):
    print('Você \033[1;36mganhou!\033[m O computador escolheu tesoura!')

#grupo usuário papel
elif(escolha=='papel' and rnd=='tesoura'):
    print('Você \033[1;31mperdeu!\033[m O computador escolheu tesoura.')
elif(escolha=='papel' and rnd=='papel'):
    print('Vocês \033[1;33mempataram!\033[m Ambos escolheram papel.')
elif(escolha=='papel' and rnd=='pedra'):
    print('Você \033[1;36mganhou!\033[m O computador escolheu pedra.')

#grupo usuário tesoura
elif(escolha=='tesoura' and rnd=='pedra'):
    print('Você \033[1;31mperdeu!\033[m O computador escolheu pedra.')
elif(escolha=='tesoura' and rnd=='tesoura'):
    print('Vocês \033[1;33mempataram!\033[m Ambos escolheram tesoura.')
elif(escolha=='tesoura' and rnd=='papel'):
    print('Você \033[1;36mganhou!\033[m O computador escolheu papel.')

else:
    print('O valor digitado não é válido.')
