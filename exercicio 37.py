#Escreva uma programa que leia um número
#qualquer e peça para o usuário escolher
#qual será escolher qual será a base da conversão:
#-1 para binário a
#-2 para octal
#-3 hexadecimal
import math
s = int(input('Digite um nùmero inteiro para a conversão'))
print("""
[ 1 ] Para converter para binário
[ 2 ] Para converter para octal
[ 3 ] Para converter para hexadecimal""")
e = int(input('Sua escolha:'))
if   e == 1:
    c = bin(s)
    print('Sua coversão de {} para {}'.format(s , c.replace('0b', 'Binário é ')))
elif e == 2:
    c = oct(s)
    print('Sua coversão de {} para {}'.format(s , c.replace('0o','Octal é ')))
elif e == 3:
    c = hex(s)
    print('Sua coversão de {} para {}'.format(s , c.replace('0x', "Hexadecimal é ")))
else:
    print('Essa escolha é enexistente!')


