# faça um programa que tenha uma função chama maios(), que receba vários
# parâmetros com valores inteiros.
# seu pragrma tem que analisar todos os valores
# e dizer qual é o maios.
valores = []
from random import  randint
def maior (v):
  print(f'{20*"=-"}\nAnalisando os valores passados...')
  for c in range(v):
      valores.append(randint(0, 10))
      print(valores[c], end=' ')
  if v == 0:
      c = -1
      valores.append(0)
  print(f'Foram informados {c+1} valores ao todo.\nO maior valor informado foi {max(valores)}.')
  valores.clear()


maior(6), maior(3), maior(2), maior(1), maior(0)
#segundo modo====================================================================================
from time import sleep
def maior(*num):
    print(f'{20 * "=-"}\nAnalisando os valores passados...')
    for n, v in enumerate(num):
        print(v, end=' ')
        sleep(0.5)
        if n == 0:
            m = v
        else:
           if m < v:
            m = v
    if len(num) == 0:
        n = -1
        m = 0
    print(f'Foram informados {n + 1} valores ao todo.\nO maior valor informado foi {m}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
