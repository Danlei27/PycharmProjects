#melhore o DESAFIO 061, para o usuario se
# ele quer mostrar mais alguns termos. O programa
#  encerra quando ela disser que quer mostrar
#  0 termos.
print(' Gerador de PA\n',7*'=-')
a1 = int(input('Primeiro  termo: '))
r = int(input('Razão da PA: '))
print('Os dez primeiros termos dessa PA são: ')
cont = 0
while cont != 10:
    cont += 1
    print('{}'.format(a1),end=' → ')
    a1 += r
m = int(input('Acabou!\nMais quantos termo você quer ver?'))
termos = cont
cont = 0
while not cont == m:
     termos += 1
     cont += 1
     print('{}'.format(a1), end=' → ')
     a1 += r
     if cont == m:
       m = int(input('Acabou\nMais quantos termo você quer ver?'))
       cont = 0
print('FIM\n Progresso finalizado com {} termos'.format(termos))
#segundo modo --------------------------------------------------
a1 = int(input('Primeriro termo: '))
r = int(input('A razão da PA: '))
cont = 10
termos = 0
while not cont == 0:
    print(a1,end=' → ')
    cont += -1
    termos += 1
    a1 += r
    if cont == 0:
      cont = int(input('Acabou!\nMais quanto termos você quer ver?:'))
print('FIM\n Progresso finalizado com {} termos'.format(termos))
