#Faça um programa que leia 5 valores nùmericos
# e guarde-os em uma lista.
#no final, mostre qual foi o maior e o menor
# valor digitado e as suas respectivas posiçoes na lista.
c = []
for v in range(1,6):
   c.append(int(input(f'{"Digite o {}ª valor":*^25}\n→'.format(v))))
print(f'Os números da sua lista são: {c}\nO maior foi {max(c)} nas posições ',end='...')
for pos in range(0,len(c)):
    if max(c) == c[pos]:
        print(pos,end='...')
print(f'\nO menor foi {min(c)} nas posições ',end='')
for pos in range(0,len(c)):
    if min(c)== c[pos]:
        print(pos,end='...')
#segundo modo-------------------------------------------------------------------------------------
from random import randint
valor = []
for c in range(1,6):
  valor.append(randint(0,10))
menor = valor[:]
maior = valor[:]
for c in range(1,5):
  if menor[0] > menor[1]:
      del menor[0]
  else:
      del menor[1]
  if maior[0] < maior[1]:
      del maior[0]
  else:
      del maior[1]
print(f'Os nvalores digitados foram {valor}\nO maior é {maior[0]}, nas posições' ,end=' ')
for pos in range(0,len(valor)):
       if maior[0] == valor[pos]:
           print(pos,end='...')
print(f'\nO maior é {menor[0]}, nas posições',end=' ')
for pos in range(0, len(valor)):
    if menor[0] == valor[pos]:
        print(pos,end='...')
#terceiro modo----------------------------------------------------
from random import randint
valor = []
for c in range(1,6):
    valor.append(randint(1,10))
menor = valor[:]
maior = valor[:]
for c1 in range(1,5):
  if menor[0] > menor[c1]:
    menor[0] = menor[c1]
  if maior[0] < maior[c1]:
    maior[0] = maior[c1]
print(f'Você digitou os seguintes valores : {valor}\nO maior valor {maior[0]}, nas posições ',end='')
for pos in range(0, len(valor)):
    if maior[0] == valor[pos]:
        print(pos,end='...')
print(f'\nO menor valor {menor[0]}, nas  posições ',end='')
for pos in range(0, len(valor)):
    if menor[0] == valor[pos]:
        print(pos,end='...')
#Quarto modo-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
valor1 = []
maior = []
menor = []
for c in range(0,5):
    valor1.append(int(input(f'{"Digite o valor na posição  {}":*^25}\n→'.format(c))))
valor2 = valor1[:]
valor2.sort()
for cont in range(0,5):
    if valor2[-1] == valor1[cont]:
        maior.append(cont)
    if valor2[0] == valor1[cont]:
        menor.append(cont)
print(f'Os valores digitados foram : {valor1}\nO maior foi {valor2[-1]} nas posições ',end='')
for maior in maior:
 print(maior,end='...')
print(f'\nO menor foi {valor2[0]} nas posições ',end='')
for menor in menor:
 print(menor,end='...')

