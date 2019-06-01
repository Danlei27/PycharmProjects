#Crie um programa que leia dois valores e mostre um menu na tela:
#[1] somar
#[2] multiplicar
#[3] maior
#[4] novos números
#[5] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso
n1 = int(input('Digite um nùmero:'))
n2 = int(input('Digite novamente mais um nùmero:'))
e = ''
while e != 5:
    e = int(input("""[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos nùmeros
[5] Sair do Programa
→Qual é sua opção ?"""))
    while e == 4:
        n1 = int(input('Digite um nùmero:'))
        n2 = int(input('Digite novamente mais um nùmero:'))
        e = 0
    if e == 1:
        escolha = n1 + n2
        print('Soma entre {} + {} = {}'.format(n1, n2, escolha))
    elif e == 2:
        escolha = n1 * n2
        print('Multiplicação entre {} x {} = {}'.format(n1, n2, escolha))
    elif e == 3:
        if n1 >= n2:
            escolha = n1
        elif n2 >= n1:
            escolha = n2
        print('O maior entre {} e {} è {} '.format(n1, n2, escolha))
    print(10 * '=-=')
print('Fim')
#Segundo modo-------------------------------------------------------------
n1 = int(input('Digite um nùmero:'))
n2 = int(input('Digite novamente mais um nùmero:'))
e = ''
while e != 5:
    e = int(input("""[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos nùmeros
[5] Sair do Programa
→Qual é sua opção ?"""))
    while e == 4:
        n1 = int(input('Digite um nùmero:'))
        n2 = int(input('Digite novamente mais um nùmero:'))
        e = 0
    while e == 1:
        escolha = n1 + n2
        print('Soma entre {} + {} = {}'.format(n1, n2, escolha))
        e = 0
    while e == 2:
        escolha = n1 * n2
        print('Multiplicação entre {} x {} = {}'.format(n1, n2, escolha))
        e = 0
    while e == 3:
        e = 0
        if n1 >= n2:
            escolha = n1
        elif  n2 >= n1:
            escolha = n2
        print('O maior entre {} e {} è {} '.format(n1, n2, escolha))
    print(10 * '=-=')
print('Fim')
