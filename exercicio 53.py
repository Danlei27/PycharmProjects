# Crie uma programa que leia uma frase
# qualquer e diga se ela é um palindromo,
# desconsideirando os espaços.
# ex
#apos a sopa
#a sacada da casa
# a torre da derrota
# o lobo ama o bolo
# anotaram a data da maratona
f= str(input('Digite uma frase: ').replace(' ','')).upper()
d = 0
f2 = len(f)
g = '\nA frase digitada acima, SIM é um palidromo!'
print('O inverso de {} é'.format(f),end=' ')
for c in range(f2-1,-1,-1):
    d += 1
    ff1 = f[d-1]
    ff2 = f[c]
    print('{}'.format(ff2),end='')
    ff3 = ff1 == ff2
    if ff3 == False:
        g ='\nA frase digitada acima, NÂO  é um palidromo!'
print(g)
#segundo modo--------------------------------------------------------
f = str(input('Digite uma frase:')).replace(' ','').upper()
# o inverso pode ser tambem com fatiamento de strings com o c[::-1]
inverso = ''
for c in range(len(f)-1,-1,-1):
    inverso += f[c]
print('O inverso de {} é {}'.format(f,inverso))
if inverso == f:
    print('Temos um palìdromo!')
else:
    print('Não temos um palìndromo!')













