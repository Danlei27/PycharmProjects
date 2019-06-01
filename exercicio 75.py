# desenvolva um progrma que leia quatro valores pelo teclado e guarde-os
# em uma tupla. no final, mostre:
# a)Quantas vezes apareceu o valor 9.
# b)Em que posicão foi digitado o primeiro valor 3.
# c)Quais foram os nùmeros pares.
cont = 0
t = (int(input('Digite um nùmero:')),
     int(input('Digite mais  um nùmero:')),
     int(input('Digite um outro nùmero:')),
     int(input('Digite o ultimo nùmero:')))
print(f'Você digitou Os valores: {t}\nO valor nove apareceu {t.count(9)} vezes')
print(f'O primeiro valor  3 foi digitado na  {t.index(3)+1}ª posição')
print(f'Os valores  pares digitado foram ',end='')
for par in t:
  if par % 2 == 0:
      print(par,end='')
#segundo modo--------------------------------------------------------------------------
valores = (int(input('Digiite um valor: ')),
           int(input('Digite mais um valor: ')),
           int(input('Digite outro valor: ')),
           int(input('Digite o ultimo valor: ')))
print(f'Você digitou os valores {valores}')
print(f'O valor nove foi digitado {valores.count(9)} vezes')
print(f'O primeiro valor 3 foi digitado na {valores.index(3)+1}'if 3 in valores else 'Nenhum valor 3 foi dgitado.')
print(f'Os valores pares são ',end='')
for par in valores:
    if par % 2 == 0:
        print(par,end=' ')


