from random import randint
from time import sleep
posibilidades = ('pedra', 'papel', 'tessoura')
computador = randint (0,2)
print('''SUAS OPÇOES:
[0] pedra
[1] papel
[2] tessoura''')
user = int(input('QUAL SUA JOGADA?\n'))
print('***PEDRA***')
sleep(0.8)
print('***PAPEL***')
sleep(0.8)
print('***TESSOURA***')
sleep(0.8)
print('-='*15)
print('O COMPUTADOR JOGOU {}'.format(posibilidades[computador]))
print ('O JOGADOR JOGOU {}'.format(posibilidades[user]))
print('-='*15)
if computador == 0:
    if user == 0:
        print ('*'*10)
        print ('EMPATE')
        print ('*'*10)
    elif user == 1:
        print ('*'*10)
        print (' VOCÊ GANGOU!!!')
        print ('*'*10)
    elif user == 2:
        print ('*'*15)
        print (' VOCÊ PERDEU :(')
        print ('*'*15)
    else:
        print('JOGADA INVÁLIDA!!!!!aAAAAA ')
elif computador == 1:
    if user == 0:
        print ('*'*15)
        print ('VOCÊ PERDEU :(')
        print ('*'*15)
    elif user == 1:
        print ('*'*10)
        print (' EMPATE')
        print ('*'*10)
    elif user == 2:
        print ('*'*10)
        print ('VOCÊ GANGOU!!!')
        print ('*'*10)
    else :
        print('JOGADA INVÁLIDA!!!!!aAAAAA ')
elif computador == 2:
    if user == 0:
        print ('*'*10)
        print ('VOCÊ GANGOU!!!')
        print ('*'*10)
    elif user == 1:
        print ('*'*15)
        print ('VOCÊ PERDEU :(')
        print ('*'*15)
    elif user == 2:
        print ('*'*10)
        print ('EMPATOU')
        print ('*'*10)
    else :
        print('JOGADA INVÁLIDA!!!!!aAAAAA ')
