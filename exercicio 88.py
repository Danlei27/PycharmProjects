#Faça um progrma que ajude um jogador da mega sena a criar palpites.
#O progrma vai perguntar quantos jogos serão gerados e vai sortear 6
#números entre 1 e 60 para cada jogo, cadrastrando tudo em uma lista composta.
from time import sleep
from random import randint
palpites = []
jogos = int(input('{:-^80}\nQuantos jogos você quer que eu  sorteie?'.format('\n     JOGA NA MEGA SENA\n')))
for j in  range(1, jogos+1):
    while len(palpites) != 6:
        num = randint(1,60)
        palpites.append(num)if palpites.count(num) == 0 else []
    print(5*'=-',f'SORTEANDO {jogos} JOGOS',5*'-=',f'\nJogo {j}: {sorted(palpites)}')if j == 1 else print(f'Jogo {j}: {sorted(palpites)}')
    palpites.clear()
    sleep(1)
print(5*'=-','< BOA SORTE! >',5*'-=')
