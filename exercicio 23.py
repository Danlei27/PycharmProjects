#faça um programa que leia um número de
#0 a 9999 e mostre na tela cada um dos
#digitos separados.

#ex:
#digite um número:1834
#unidade: 4
#dezenas:3
#centena:8
#milhar:1

#primero-----------------------------------------------------------------------------------
a=int(input('numero'))
print('unidade{}'.format (a//1%10))
print('dezena{}'.format  (a//10%10))
print('centena{}'.format (a//100%10))
print('milhar{}'.format  (a//1000%10))
# segundo-----------------------------------------------------------------------------------
import math
a=int(input('numero'))
e1=a/10000
e2=math.floor(e1)
e3=e1-e2
print('Milhar',math.trunc (e3*10.000))

b1=a/1000
b2=math.floor(b1)
b3=b1-b2
print('Centena',math.trunc(b3*10.007))

d1=a/100
d2=math.floor(d1)
d3=d1-d2
print('Dezena',math.trunc (d3*10.007))

c1=a/10
c2=math.floor(c1)
c3=c1-c2
print('Unidade',math.trunc(c3*10.007))
#-------------------------------------------------------------------------------------
#terceiro com strings
a=str(input('numero:'))

bb5=a[3:4]+a[2:3]+a[1:2]+a[0:1]+'0000'

#1==1*12==21*123==321*1234==4321

bb1=bb5 [3:4]
bb2=bb5 [2:3]
bb3=bb5 [1:2]
bb4=bb5 [0:1]

print('milhar    {} '.format(bb1))
print('centena   {} '.format(bb2))
print('dezena    {} '.format(bb3))
print('unidade   {} '.format(bb4))








