#crie um programa que simule o funcionamento de um caixa eletronico
#no inicio qual será o valor a ser sacado (Números inteiro)e o programa
#vai informar quantas Cédulas de cada valor serão entregues.

#obs: Consideirandre que o caixa possui
#  cédulas de R$50, R$20, R$10 e R$1.
q = int(input('Digite o valor a ser sacado R$: '))
nota50 = nota20 = nota10 = nota1 = 0
cont = 0
while True:
    while not q < 50  :
        cont += 1
        while cont == 50:
          nota50 += 1
          q += -50
          cont = 0
    while not q < 20:
        cont += 1
        while cont == 20:
          nota20 += 1
          q += -20
          cont = 0
    while  not q < 10:
        cont += 1
        while cont == 10:
           nota10 += 1
           q += -10
           cont = 0
    while q <= 9 and  not q <= 0:
        cont += 1
        while cont == 1:
           nota1 += 1
           q += -1
           cont = 0
    break
print(f'{nota50} Cédulas de 50R$') if nota50 >= 1 else ''
print(f'{nota20} Cédulas de 20R$') if nota20 >= 1 else ''
print(f'{nota10} Cédulas de 10R$') if nota10 >= 1 else ''
print(f'{nota1} Cédulas de 1R$')   if nota1  >= 1 else ''
#segundo modo ----------------------------------------------
s = int(input('{:~^20}\nDgite o valor a ser sacado: '.format('Banco CEV')))
if s // 50 >= 1:
   n50 = s // 50
   s += (-50 * n50)
   print(f'{n50} Cédulas de 50R$')
if s // 20 >= 1:
   n20 = s // 20
   s += (-20 * n20)
   print(f'{n20} Cédulas de 20R$')
if s // 10 >= 1:
   n10 = s // 10
   s += (-10 * n10)
   print(f'{n10} Cèdulas de 10R$')
if s // 1 >= 1:
   n1 = s // 1
   s += (-1 * n1)
   print(f'{n1} Cédulas de 1R$')
#terceiro modo--------------------------------------------
v = (int(input('Digite o valor a ser sacado :')))
notaatual = 50
totcéd = 0
while True:
    if v >= notaatual:
        v -= notaatual
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'{totcéd} Cédula de R${notaatual}'if totcéd == 1 else (f'{totcéd} Cédulas de R${notaatual}'))
            totcéd = 0
        if notaatual == 50:
            notaatual = 20
        elif notaatual == 20:
            notaatual = 10
        elif notaatual == 10:
            notaatual = 1
        if v == 0:
            break
