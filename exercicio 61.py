#Refaça o DESAFIO 051,lendo o primeiro termo
#  e a razão de uma PA, mostrando os 10 primeiros
#  termos da progressão usando  a estrutura while.
print(' Gerador de PA\n',7*'=-')
a1 = int(input('Primeiro  termo:'))
r = int(input('Razão da PA:'))
print('Os dez primeiros termos dessa PA são:')
n = 0
while n != 10:
    n += 1
    print('{}'.format(a1),end=' → ')
    a1 += r
print(' Acabou')

