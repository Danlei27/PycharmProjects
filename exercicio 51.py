# Desenvolva um programa que leia o
#primeiro termo e a razão de uma PA.
# no final, mostre os 10 primeiros
# termos dessa progressão.
a1 = int(input('Digite o primeiro termo da PA:'))
r = int(input('Digite a razão da PA:'))
print('Os dez primeiros termos dessa PA são:\n',a1,end=' → ')
for n in range(1,10):
    a1 += r
    print(a1,end=' → ')
print('ACABOU')
# segunda forma→→→→-----------------------------------------
a1 = int(input('Digite o primeiro termo da PA:'))
r = int(input('Digite a razão da PA:'))
print('Os dez primeiros termos dessa PA são:')
an = a1 + (10-1)*r
for a in range(a1, an + r, r,):
    print(' {}'.format(a),end=' →')
print(' ACABOU')
