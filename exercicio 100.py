# faça um programa que tenha uma lista chama números
# e duas funções chamadas sorteia() e somapar().A primeira
# função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função
# vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
números = []
from time import sleep
from random import randint


def sorteia(v):
    print(f'Sorteando {v} valores da lista: ', end='')
    for c in range(0, v):
        números.append(randint(0, 10))
        print(números[c], end=' ')
        sleep(0.6)
    print(f'PRONTO!')


def somapar():
    resultado = 0
    for par in números:
        if par % 2 == 0:
            resultado += par
    print(f'Somando os valores pares de {números}, temos {resultado}.')


sorteia(5)
somapar()
