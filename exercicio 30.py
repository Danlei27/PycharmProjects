#crie um Programa que leia uma numero inteiro e mostre na tela
#na tela se ele é PAR ou IMPAR.
import parser

n=int(input('digite o número para ser feita a leitura de Par ou Impar:'))
n1=n/2
n2=str(n1)
n3='.5' in n2
if n3 == True:
    print(' O número {} è Ìmpar.'.format(n))

else:
    print('O número é {} Par.'.format(n))

#Segundo modo!----------------------------------------------------------------------------------
n=int(input('digite o número para ser feita a leitura de Par ou Impar:'))
n1=n%2
if n1==1:
    print('O número {} Ímpar.'.format(n))
else:
    print('O número é {} Par.'.format(n))