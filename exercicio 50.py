#desenvolva um programa que leia seis
#  nùmeros inteiros e mostre a soma
# apenas daqueles que forem pares.
# se o valor digitado for impar,
# desconsidere-o.
s = 0
c = 0
for n in range(1, 7):
 n = int(input('nùmero {}:'.format(n)))
 if n %2 == 0:
     s += n
     c += 1
print('Nùmero digitados pares é {}.\nA soma dos  os nùmeros pares são {}'.format(c,s))