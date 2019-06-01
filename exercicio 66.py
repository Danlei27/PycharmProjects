# Crie um programa que leia vários Números inteiros
# pelo teclado. O programa sò vai parar quando o usuário digitar
# o valor 999, que é a condicão de parada. No final, mostre quantos
#Números foram digitados e qual foi a soma entre eles (desconsideirando o flag).
soma = cont = 0
while True :
    n = int(input('Digite um Nùmero[digite 999 para PARAR!]: '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'Você digitou {cont} números  e a soma foi {soma}.')