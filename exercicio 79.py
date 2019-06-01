#Crie um programa  onde o usuario possa digitar vários
#valores nùmericos e cadastre-os em uma lista.Caso on
#nùmero já exista lá dentro, ele não será adicionado.
#No final, serão exibidos todo os valores únicos digitados,
# em ordem crescente.
valor = []
r = 'S'
cont = 0
while True:
        if r in 'N':
            break
        while  r in 'S':
            valor.append(int(input('Digite um valor: ')))
            if  valor.count(valor[cont]) == 1 :
                print('Salvo com sucessso...!')
                cont+=1
            else:
                print('Valor duplicado não vou adicionar...!')
                del valor[cont]
            r = ' '
            while not  r in 'SN':
              r = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
print(f'Você digitou os valores {sorted(valor)}')
#segundo -----------------------------------------------------------------
valor = []
r = 'S'
while True:
     if r == 'N':
        break
     while r in 'S':
      valor.append(int(input('Digite um nùmero: ')))
      if valor.count(valor[-1]) != 1:
          print(f'O valor {valor[-1]} já foi digitado!!!')
          del valor[-1]
      else:
          print(f'O valor {valor[-1]} adicionado com sucesso...!')
      r = ' '
      while not  r in 'SN':
        r = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
print(f'Os valores digitados foram {sorted(valor)}')
#terceiro modo---------------------------------------------------------
valores = []
while True:
    n = int(input('Digite um valor: '))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado, não vou adicionar!')
    r = str(input('Quer continuar [S/N] :'))
    if r in 'Nn':
        break
print(f'Os valores adicionados foram {sorted(valores)}')


