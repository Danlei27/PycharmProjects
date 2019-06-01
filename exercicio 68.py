# Faça um programa que jogue par ou impar com
# o computador jogo só será interrompido quando o jogador perder, mostrando o total,
# de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
print('Vamos jogar! PAR  ou  IMPAR!')
v = 0
while True:
    pc = randint(1, 10)
    jo = int(input('Escolha um nùmero: '))
    e = str(input('Par ou Impar [P/I]: ')).upper().strip()[0]
    while not e in 'PI':
      e = str(input('Par ou Impar [P/I]: ')).upper().strip()[0]
    if e == 'I':
        if (pc + jo) % 2 != 0:
            v += 1
            print(f'Você venceu  deu Impar! pc {pc} e você {jo} total deu {pc + jo}')
        else:
          r = 'Par'
          break
    if e == 'P':
        if (pc + jo) % 2 == 0:
            v += 1
            print(f'Você venceu  deu Par! pc {pc} e você {jo} total deu {pc + jo}')
        else:
          r = 'Impar'
          break
print(f'Voce jogou {jo} e o Pc {pc} total deu  {jo + pc} {r}\nVocê perdeu!')
print(f'GAMER OVER! Você venceu {v} vezes.')
#segundo modo ----------------------------------------------------------------
from random import randint
print('Vamos jogar PAR ou IMPAR!')
v = 0
while True:
    pc = randint(0,10)
    jo = int(input('Digite um nùmero: '))
    e = ' '
    total = pc + jo
    while not e in 'PI':
        e = str(input('Escolha Par ou Impar [P/I]: ')).upper().strip()[0]
    r = ('Par'if total % 2 == 0 else 'impar')
    if e == 'P':
        if total % 2 == 0:
            print(f'\033[33mVocê venceu! Pc jogou {pc} e Você {jo} total deu {total} deu {r}\033[m')
            v += 1
        else:
            break
    elif e == 'I':
        if total % 2 != 0:
            print(f'\033[33mVocê venceu! Pc jogou {pc} e Você {jo} total deu {total} deu {r}\033[m')
            v += 1
        else:
            break
print(f'\033[31mVocê perdeu! Pc jogou {pc} e Você {jo} o total foi {total} deu {r}\n\033[34mVocê venceu {v} vezes.')
