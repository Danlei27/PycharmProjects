#cont = 1
#while True:
#    print(cont,end=' → ')
#   cont += 1
#print('Acabou!')
## aula sobre o break
n = s = 0
while True:
   n = int(input('Digite um nùmero: '))
   if n == 999:
       break
   s += n
print(f'A soma vale {s}')
## aula sobre fstrings
oi = 'Oi mundo'
print(f'{oi}')
print('{}'.format(oi))
nome = 'Danlei'
idade = 24
salario = 987.3
print(f'O {nome:-^20}')
print(f'O {nome:*<20} tem {idade} anos e ganha {salario:.2f} R$ ')
print(f'{nome:+>20}')