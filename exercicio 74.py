# Crie um programa que vai gerar cinco nùmeros aleatórios
# e colocar em uma tupla.
# depois disso, mostre a listagem de nùmeros gerados e também
# indique o menor e o maior valor que estão na tupla.
from random import randint
c = 0
t = (randint(0, 10), randint(0, 10), randint(0, 10),randint(0, 10),randint(0, 10))
print(t)
for tupla in t:
    c += 1
    if c == 1:
        menor = tupla
        maior = tupla
    else:
        if menor > tupla:
            menor = tupla
        if maior < tupla:
            maior = tupla
print(f'O maior valor é {maior}\nO menor valor é {menor}')
#segundo modo------------------------------------------------
from random import randint
c = 0
print(f'Os números sorteados são : ',end='')
while c != 5:
        tupla = randint(0,10)
        c += 1
        if c == 1:
            menor = tupla
            maior = tupla
        else:
            if menor > tupla:
                menor = tupla
            if maior < tupla:
                maior = tupla
        print(tupla,end=' ')
print(f"\nO maior valor é {maior}\nO menor valor é {menor}")
#terceiro modo ---------------------------------------------
from random import randint
t = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
print('os nùmeros sorteados foram : ',end='')
for num in t:
    print(num,end=' ')
print(f'\nO maior valor foi {max(t)}')
print(f'O menor valor foi {min(t)}')


