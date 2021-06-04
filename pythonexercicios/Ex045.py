from random import randint
from time import sleep
itens = ('pedra','papel', 'tesoura')
computador = randint(0, 2)
print(''' Suas opções:
[ 1 ]PEDRA
[ 2 ]PAPEL
[ 3 ]TESOURA''')
jogador = int(input('Qual é a sua jogada?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
print("-="*11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)
if computador == 0:#computador jogou PEDRA
  if jogador == 0:
     print('Empatou')
  elif jogador == 1:
     print('Jogador Ganhou')
  elif jogador == 2:
     print('Computador Ganhou')
  else:
     print('Jogada Inválida')
elif computador == 1: #computador jogou PAPEL
    if jogador == 0:
        print('Computador Ganhou!')
    elif jogador == 1:
        print('Empatou!')
    elif jogador == 2:
        print('Jogador Ganhou!')
    else:
        print('Jogada Inválida!')
elif computador == 2:#computador jogou tesoura
    if jogador == 0:
       print('jogador ganhou!')
    elif jogador == 1:
       print('Computador Ganhou!')
    elif jogador == 2:
       print('Empatou!')
    else:
        print('Jogada Inválida')


