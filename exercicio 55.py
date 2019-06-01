# Faça um programa que leia o peso de cinco
# pessoas. no final, mostre qual foi o maior
#  e menor pesso lidos.
for c in range(1,5):
    p = float(input('Peso da {}ª pessoa:'.format(c)))
    if c == 1:
        p1 = p
    elif c == 2:
        p2 = p
        if p2 > p1:
            maior = p2
        else:
            maior = p1
        if p2 < p1:
            menor = p2
        else:
            menor = p1
    elif c == 3:
        p3 = p
        if p3 > maior:
            maior = p3
        if p3 < menor:
            menor = p3
    elif c == 4:
        p4 = p
        if p4 > maior:
            maior = p4
        if p4 < menor:
            menor = p4
print('O maior pesso lido foi {}Kg\nO menor pesso lido foi {}Kg'.format(maior,menor))
# segundo modo-----------------------------------------------------------------------
maior = 0
menor = 0
for c in range(1,6):
    peso = float(input('Peso da {}ª pessoa'.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi {}Kg'.format(maior))
print('O menor peso lido foi {}Kg'.format(menor))
