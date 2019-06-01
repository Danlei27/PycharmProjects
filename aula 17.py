num = (2, 5, 9, 1)
print(num)
#tuplas são imutaveis (num[2] = 3) não funciona
num = [2, 5, 9, 1,]
print(num)
num[0] = 10# adicionando 10 na posição 0
print(num)
num.append(99)# adicionando um valor na ultima posição
print(num)
num.sort()# deixa em ordem
print(num)
num.sort(reverse=True)#vai inverter a ordem
print(num)
print(f'Essa lista tem {len(num)} elementos.')
num.insert(0,444)# vai ser inserida na posição escolhida, o valor solicitado
print(f'Essa lista tem {len(num)} elementos.')
print(num)
num.pop()#Remove o ultimo valor
print(num)
num.pop(2)#Remove item da posição desejada
print(num)
num.remove(99)#removeu o elemento desejado
print(num)
valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for v in valores:
    print(f'{v}...')
for pos, v in enumerate(valores):
    print(f'na poição {pos} encontrei {v}!')
print('FIM')
a = [2, 3, 4, 7]
b = a
b[2] = 8
print(f'lista {a}\nLista {b}')
a2 = [2, 3, 4, 7]
b2 = a[:]#CÓPIA DOS VALORES DE A
b2[2] = 8
print(f'Lista {a2}\nlista {b2}')