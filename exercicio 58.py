#Melhore o jogo do DESAFIO 028 onde o computador
#  vai "pensar" em um nùmero entre 0 e 10. Sò
# que agora o jogador vai tentar adivinhar até
# acertar, mostrando no final quantos palpites
# foram necessàrios para vencer.
eu = '0'
pc = '1'
r = 0
from random import randint
print(27*'\033[32m=-')
l = print('Tente adivinhar o número que o pc está pensado 0 a 10.')
print(27*'\033[32m=-')
while eu != pc:
    pc = randint(0, 10)
    r += 1
    eu = int(input('\033[34m{}° tentativa:\033[m'.format(r)))
    print('Pc pensou no {} e você no {}  '.format(pc, eu))
print('\033[33mParabens!!! O Pc pensou no número {} e você digitou o nùmero {}'.format(pc,eu))
#segundo modo----------------------------------------------------------------------------------
from random import randint
eu = ''
p = 0
pc = randint(0,10)
print("""Sou seu computador...
Acabei de pensar em um entre 0 a 10.
Será que  você consegue adivinhar qual foi?""")
while eu != pc:
    p += 1
    eu = int(input('Qual é o seu {}.° palpite ?'.format(p)))
    if pc > eu:
        print('\033[32mMais...tente outra vez.\033[m')
    elif pc < eu:
        print('\033[36mMenos... tente outra vez.\033[m')
print('\033[35mParabens você acertou no {}.° palpite, pensei no nùmero  {}\nE  você teclou o nùmero {}'.format(p,pc,eu))
