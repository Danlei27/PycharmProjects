#"""Escreva um programa que faça o coputador "pensar" em número
# inteiro entre 0 e 5 e peça para  usuàrio tentar
# descobrir qual foi o número escolhido pelo computdor."""
#"""O  programa deverá escrever na tela se o
#usuàrio venceu ou perdeu."""
from random import randint
from time import sleep
nn=int(input('Tente descobrir qual e o número da máquina 0 a 5:'))
n=randint(0,5)
print('\033[36m''Máquina: meu número é...''\033[m')
sleep(3)
if n ==  nn:
    print('\033[34m''Parabens você venceu!')
else:
    print('\033[31m''infelizmente você perdeu!')
print('\033[33m''-=-' *20)
print( '\033[32m''Seu número é {} e o da máquina é {}'.format(nn,n))
print('\033[33m''-=-' *20)
