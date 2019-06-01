#crie um progrma que crie uma matrix de dimensão 3x3 e
#preencha com valores lidos pelo teclado.
#No final, mostre a matrix na tela, com a
#formatação correta.
from random import randint
from random import randint
filheira = filheira2 = 0
matrix = [[],[],[],]
while len(matrix[2]) != 3 :
    matrix[filheira].append(randint(0,999))
    if len(matrix[filheira]) == 3:
        filheira += 1
for cont in range(0,3):
 for pos,  c in  enumerate(matrix[filheira2]):
    print(f'[{c:^6}]',end='')
    if 2 == pos or pos == 5:
        print()
        filheira2 += 1
#segundo ==========================================
from random import randint
matrix = [[],[],[],]
for c in range(0,3):
    for cont in range(0,3):
      matrix[c].append(randint(0,999))
for cont1 in range(0,3):
 for  c1 in  matrix[cont1]:
    print(f'[{c1:^6}]',end='')
 print()
#terceiro modo=====================================
matrix = []
for con in range(0,9):
      matrix.append('[{:^6}]'.format(int(input(f'Digite um valor para [ {con//3},{con %3}]'))))
for cont in range(1,10):
  print(f'{matrix[cont-1]}\n' if cont == 3 or cont == 6 else f'{matrix[cont-1]}',end='')