# Faça um prgrama que leia um nùmero
# inteiro e diga se ele é ou não um
# nùmero primo.
d3 = 0
p = int(input('digite número'))
for d in range(1,p+1):
    d2 = p % d
    if d2 == 0:
      d2 = 1
      d3 += d2
if d3 <= 1 or d3 >= 3:
    print('O número {} não é PRIMO.'.format(p))
else:
    print('O nùmero {} è PRIMO.'.format(p))
# segundo modo-------------------------------------
d = 0
n = int(input('digite um nùmero:'))
for c in range(1,n+1):
    if  n % c == 0:
     c2 = 1
     d += c2
     c = '\033[32m{}\033[m'.format(c)
    print('\033[31m\033[m'.format(c),end=' ')
if d >= 3 or d <= 1:
  print('\nO nùmero {} foi divisivel {} vezes\nE por isso  NÃO É PRIMO!.'.format(n,d))
else:
  print('\nO nùmero {} foi divisivel {} vezes\nE por isso  È PRIMO'.format(n,d))





















