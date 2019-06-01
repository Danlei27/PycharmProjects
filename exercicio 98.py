#Faça um programa que tenha uma função chama
#contador(), que reba Tres parametros:inicio, fim e passo
#e realize a contagem.
#seu programa tem que realizar tres contagens através da função
#criada:
#a) de 1 até 10, de 1 em 1
#b) de 10 até 0, de 2 em 2
#c)Uma contagem pesonalizada.
from time import sleep
def contador(num):
    print(num,end=' ')
    sleep(0.2)


print(f'{20*"=-"}\nContagem de 1 até 10 de 1 em 1.')
for c in range(1, 11):
    contador(c)
print(f'FIM!\n{20*"=-"}\nContagem de 10 até 0 de 2 em 2.')
for c in range(10, -1, -2):
    contador(c)
inicio = int(input(f'FIM!\n{20*"=-"}\nAgora é sua vez de personalizar a contagem!\nInicio: '))
fim = int(input('Fim: '))
p = int(input('Passo: '))
print(f'{20*"=-"}\nContagem de {inicio} até {fim} de {p} em {p}')
if inicio > fim:
    contador(inicio)
    while not inicio <= fim:
        if p > 0:
            inicio -= p
            contador(inicio)
        else:
            inicio += p
            contador(inicio)
else:
    for c in range(inicio, fim+1, p):
        contador(c)
print('FIM!')
#segundo modo ===========================================================================================
from time import sleep


def escreve(inicio, fim, passo):
    print(f'{20 * "=-"}\ncontagem de {inicio} até {fim} de {passo} em {passo}')


def contador(num):
    print(num, end=' ')
    sleep(0.5)


escreve(1, 10, 1)
for num in range(1, 11):
    contador(num)
print('FIM!')
escreve(10, 0, 2)
for num in range(10, -1, -2):
    contador(num)
inicio = int(input(f'FIM!\n{20 * "=-"}\nAgora é sua vez de personalizar a contagem!\nInicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
escreve(inicio, fim, passo)
if inicio < fim:
    for num in range(inicio, fim, passo):
        contador(num)
else:
    while inicio >= fim:
        contador(inicio)
        if passo > 0:
            inicio -= passo
        else:
            inicio += passo
print('FIM!')
#terceiro  modo ========================================================================================
from time import sleep
def escreve(inicio, fim, passo):
    print(f'{20*"=-"}\ncontagem de {inicio} até {fim} de {passo} em {passo}')


def contador(inicio, fim, passo,):
    if inicio < fim:
        for num in range(inicio, fim+1, passo):
            print(num, end=' ')
            sleep(0.5)
    else:
        while inicio >= fim:
            print(inicio, end=' ')
            sleep(0.5)
            if passo > 0:
                inicio -= passo
            else:
                inicio += passo
    print('FIM!')


escreve(1, 10, 1)
contador(1, 10, 1)
escreve(10, 0, 2)
contador(10,-1, -2)
inicio = int(input(f'{20*"=-"}\nAgora é sua vez de personalizar a contagem!\nInicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
escreve(inicio, fim, passo)
contador(inicio, fim, passo)
# ultimo modo--------------------------------------------------------------------------------
from time import sleep
def contador(inicio, fim, passo,):
    if passo == 0:
        passo = 1
    if passo < 0:
        passo *= -1
    print(f'{20 * "=-"}\ncontagem de {inicio} até {fim} de {passo} em {passo}')
    if inicio < fim:
        while not  inicio > fim:
            print(inicio, end=' ')
            sleep(0.5)
            inicio += passo
    else:
        while not inicio < fim:
            print(inicio, end=' ')
            sleep(0.5)
            inicio -= passo
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
inicio = int(input(f'{20*"=-"}\nAgora é sua vez de personalizar a contagem!\nInicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
