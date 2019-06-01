# Crie um programa que tenha uma tupla totalmente preenchida com uma
# contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado(entre 0 e 20)
# e mostrà-lo por extenso.
extenso = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze',
'Cartoze', 'Quinze', 'Dezesseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte')
cont = 0
c = 'S'
while True:
      if c == 'N':
        break
      n = int(input('Digite um número entre 0 e 20: 'if cont == 0 else 'Tente novamente.Digite um número entre 0 e 20: '))
      cont += 1
      while 0 <= n <= 20:
       print(f'O nùmero digitado foi {extenso[n]}')
       cont = 0
       n = 21
       c = ' '
       while not c in 'SN':
        c = str(input('Quer continuar [S/N]')).strip().upper()[0]
print('FIM')
#segundo modo ------------------------------------------------------------------------------------------------------------
extenso = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze',
'Cartoze', 'Quinze', 'Dezesseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte')
c = ' '
while True:
    if c == 'N':
        break
    n = int(input('Digite um número: '))
    while 0 <= n <= 20:
        print(f'O número digitado foi {extenso[n]}')
        n = 21
        c = ' '
        while not c in 'SN':
           c = str(input('Quer continuar?: ')).upper().strip()[0]
print('FIM')
