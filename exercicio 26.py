#Faça um programa que leia uma
#frase pelo teclado e mostre:

#Quantas vezes aparece a letra"A".
#Em que posção ela aparece a primeira vez.
#Em que posição ela aparece a útltima vez.

a=str(input('Escreva uma frase').strip().upper())
print(a)
print('A letra A aparece {}, vezes'.format(a.count('A')))
aa=a.split('A')
g=len(aa[len(aa)-1])
g2=len(a)-g
print('A primera vez ela aparece na posição {}'.format((a.find('A')+1)))
print('E a sua ultima posição è {}'.format(g2))
print('O total de caracteres da frase è {}'.format(len(a)))
#outra opção---------------------------------------------------------------------
a=str(input('Escreva uma frase').strip().upper())
print(a)
print('A letra A aparece {}, vezes'.format(a.count('A')))
print('A primera vez ela aparece na posição {}'.format((a.find('A')+1)))
print('E a sua ultima posição è {}'.format(a.rfind('A')+1))
print('O total de caracteres da frase è {}'.format(len(a)))