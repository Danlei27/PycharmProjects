#faça um programa que leia um nùmero qualquer e mostre o seu fatorial.
#ex:
#5!=5x4x3x2x1=120
f = int(input('Digite um nùmero para\nCalcular seu fatorial:'))+1
f1 = f-1
print('Claculando {}! = '.format(f1),end='')
while f != 2:
  f += -1
  f1 *= f - 1
  print('{} x '.format(f),end='')
print('1 = {}'.format(f1),end='')



#segundo modo com laço for -----------------

f = int(input('calcule o fatorial:'))+1
f1 = f-1
print('Calculando o !{} = '.format(f1),end='')
for c in range(2, f):
     f += -1
     f1 *= f-1
     print('{} x '.format(f),end='')
print('1 = {}'.format(f1),end='')



# terceiro mètodo com math-------------------
from math import factorial
f = int(input('Digite um nùmero para calcullar seu fatorial:'))
print('Calculado o !{} = '.format(f),end='')
fatorial = factorial(f)
for c in range(f ,1 ,-1):
    if c != 0 :
     print('{} x '.format(c),end='')
print('1 = {}'.format(fatorial,end=''))