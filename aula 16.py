lanche = ('Hambúrguer')
lanche = ('Suco')
print(lanche)
lanche2 = ('Hambúrguer','Suco','Pizza','Pudim')
print(lanche2[3])
print(lanche2[-4])
print(lanche2[1:3])#O ultimo nùmero é ignorado!
print(lanche2[2:])
print(lanche2[:2])#O ultimo nùmero é ignorado!
print(lanche2[-2:])
print(lanche2[-3:])
print(lanche2)
#tuplas são imutáveis
#lanche2[1] = 'Refrigerante'
#print(lanche[1])
print(len(lanche2))
for comida in lanche2:
    print(f'Eu vou comer {comida}')
#for com variável composta
print('Comi de mais!')
for cont in range(0,len(lanche2)):
    print(lanche2[cont])
print('comi muito!')
#for com range
for pos, comida in enumerate(lanche2):
    print(f'Vou comer {comida} na posisão {pos}')
for cont in range(0, len(lanche2)):
    print(f'Vou comer {lanche2[cont]}na posição {cont}')
print(sorted(lanche2))
print(lanche2)
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(len(c))
print(c.count(5))
print(c.count(9))
print(c.index(8))
print(c.index(2, 1))#deslocamento
pessoa = ('Danlei', 24, 'M', 75.0)
print(pessoa)
del(pessoa)
#tuplas são imutáveis mas podem serem  apagadas
print(pessoa)
