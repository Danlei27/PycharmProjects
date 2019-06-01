# crie um programa que faça o computador
#  jogar jokenpô com vocè.
from random import randint
from time import sleep
pc = randint(1,3)
jo = int(input('''Vamos jogar!
[1] Pedra
[2] Papel
[3] Tesoura
Qual a sua opção?'''))
print('JO...')
sleep(1)
print('KEN...')
sleep(1)
print('PÔ!!!')
if jo <= 3:
  if pc == 1 and jo == 2:
    m = ('\033[33m''você venceu!')
  elif pc == 2 and jo == 3:
    m = ('\033[33m''você venceu!')
  elif pc == 3 and jo == 1:
    m = ('\033[33m''você venceu!')
  elif pc == jo:
    m = ('\033[34m''Empate!')
  else:
    m = ('\033[31m''Você perdeu!')
  if jo <= 3:
    jo = str(jo).replace('1', 'Pedra')
    jo = str(jo).replace('2', 'Papel')
    jo = str(jo).replace('3', 'Tesoura')
    pc = str(pc).replace('1', 'Pedra')
    pc = str(pc).replace('2', 'Papel')
    pc = str(pc).replace('3', 'Tesoura')
    print('{}\nJogador {}\n PC {}'.format(m, jo, pc,))
else:
    print('opção invalida!')
# segundo modo-----------------------------------------------------------
from random import randint
from time import sleep
itens = ('Pedra','Papel','Tesoura')
pc = randint(0,2)
jo = int(input('''Vamos jogar!
[0] Pedra
[1] Papel
[2] Tesoura
Qual a sua opção?'''))
print('JO...')
sleep(1)
print('KEN...')
sleep(1)
print('PÔ!!!')
if jo <= 2:
  if pc == 0 and jo == 1:
    m = ('\033[33m''você venceu!')
  elif pc == 1 and jo == 2:
    m = ('\033[33m''você venceu!')
  elif pc == 2 and jo == 0:
    m = ('\033[33m''você venceu!')
  elif pc == jo:
    m = ('\033[34m''Empate!')
  else:
    m = ('\033[31m''Você perdeu!')
if jo <= 2:
  print('Jogador {}'.format(itens[jo]))
  print('PC {}'.format(itens[pc]))
  print(m)
else:
    print('opção invalida!')