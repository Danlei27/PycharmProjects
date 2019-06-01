# Crie um programa que leia vàrios Nùmeros inteiros pelo teclado.
# o programa sò vai parar quando o usuário digitar o valor 999,
# que é a condição de parada.No final, mostre quantos nùmeros
# foram digitados e qual foi a soma entre eles(desconsiderando o flag).
d = d2 = cont = 0
while not d == 999:
    d = int(input('Digite um nùmero [Digite 999 para PARAR!]: '))
    if d != 999:
        cont += 1
        d2 += d
print('Você digitou {} nùmero e a soma entre eles foi {}'.format(cont,d2))
#segundo modo ------------------------------------------------------------
cont = n = s = 0
n = int(input('Digite um nùmero[ Digite o nùmero 999 para PARAR!]: '))
while n != 999:
    s += n
    n = int(input('Digite um nùmero[Digite o nùmero 999 para PARA!]'))
    cont += 1
print('Você digite {} valores e soma foi {}'.format(cont,s))



