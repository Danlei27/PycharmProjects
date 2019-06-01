"""for c in range(1,10):
    print(c)
print('fim')"""
c = 0
while c < 10:
    c += 1
    print(c)
print('fim')
"""Condição de parada  só  atè que digite o '0' """
n = 1
while n != 0:
    n = int(input('Digite um valor:'))
print('fim')
n2 = 'S'
while n2 == 'S':
    v = int(input('Digite um valor:'))
    n2 = str(input(' Quer continuar [S/N] ?')).upper()
print('Fim')
n3 = 1
par = impar = 0
while n3 != 0:
    n3 = int(input('Digite um valor:'))
    if n3 !=0 :
        if n3 % 2 == 0:
            par += 1
        else:
            impar += 1
print('São {} pares e {} impares.'.format(par,impar))

print('Acabou')