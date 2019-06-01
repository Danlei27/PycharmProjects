#faça um programa que leia Tres número e mostre qual é
# o maior e qual é o menor.
n1 = int(input('Nùmero 1'))
n2 = int(input('Nùmero 2'))
n3 = int(input('Nùmero 3'))
if n1>n2>n3:
  print('O maior valor digitado   {}\nO menor  {}'.format(n1,n3))
if n1>n3>n2:
    print('O maior valor digitado  {}\nO menor  {}'.format(n1,n2))
if n2>n1>n3:
    print('O maior valor digitado  {}\nO menor {}'.format(n2,n3))
if n2>n3>n1:
    print('O maior valor digitado  {}\nO menor  {}'.format(n2,n1))
if n3>n2>n1:
    print('O maior valor digitado   {}\nO menor  {}'.format(n3,n1))
if n3>n1>n2:
    print('O maior valor digitado   {}\nO menor  {}'.format(n3,n2))

#segundo forma_--------------------------------------------------------------------
n1 = int(input('Nùmero 1'))
n2 = int(input('Nùmero 2'))
n3 = int(input('Número 3'))

menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O maior digito é {}\nO menor digito è {}'.format(maior,menor))