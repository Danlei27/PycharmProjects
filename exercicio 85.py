#Crie um programa onde o usuário possa digitar sete valores
#númericos e cadastre-os em uma lista única que matenha separados
#os valores pares e impares.No final, mostre os valores pares e impares em ordem crescente.
total = []
impar = []
par = []
for c in range(0,7):
    total.append(int(input('Digite um número: ')))
    if total[c] % 2 != 0:
        impar.append(total[c])
    else:
        par.append(total[c])
total.clear()
total.append(sorted(impar))
total.append(sorted(par))
print(f'Os valores impares são: {total[0]}\nOs pares são: {total[1]}')
#segundo modo===========================================================
total = []
impar = []
for c in range(0,7):
    total.append(int(input('Digite um número: ')))
    if total[len(total)-1] % 2 != 0:
        impar.append(total[len(total)-1])
        del total[len(total)-1]
total.append(sorted(impar))
print(f'Os valores impares são: {total[-1:]}\nOs pares são: {sorted(total[:-1])}')
#terceiro modo====================================================================
total = [[]]
for c in range(0,7):
    total.append(int(input('Digite um número: ')))
    if total[len(total)-1] % 2 != 0:
        total[0].append(total[len(total)-1])
        print(total)
        del total[len(total)-1]
print(f'Os valores impares são: {sorted(total[0])}\nOs pares são: {sorted(total[1:])}')
#Quarto modo===========================================================================
total = [[],[]]
for c in range(0,7):
    num = int(input('Digite um número: '))
    if num % 2 != 0:
        total[0].append(num)
    else:
        total[1].append(num)
print(f'Os valores impares são: {sorted(total[0])}\nOs pares são: {sorted(total[1])}')