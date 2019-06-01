#Aprimore o desafio anterior, mostrando no final:
#A) A soma de todos os valores pares digitados.
#B) A soma dos valores de terceira coluna.
#C) O maior valor da segunda linha.
matrix = []
somap =  0
for con in range(0,9):
      matrix.append(int(input(f'Digite um valor para [ {con//3},{con %3} ]:')))
      somap += matrix[con]if matrix[con] % 2 == 0 else 0
for cont in range(1,10):
  print(f'[{matrix[cont-1]:^6}]\n' if cont == 3 or cont == 6 else f'[{matrix[cont-1]:^6}]',end='')
print(f'\nA soma de todos os valores pares são: {somap}.\nA soma da terceira coluna: {matrix[2]+ matrix[5] + matrix[8]}.\nO maior valor da segunda linha é {max(matrix[3:6])}.')