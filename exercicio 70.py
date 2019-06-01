# crie um programa que leia o nome e o preço de Vários
# Produtos. O programa deverà perguntar se o usuàrio vai continuar.No final, mostre:
# A) Qual é o total gasto na compra.
# B) Quantos Produtos custam mais de 1000R$.
# C) Qual è o nome do Produto mais barato.
total = mais1k = barato= 0
q = 'S'
while True:
    while q == 'S':
        print('~~~~~~~Lojão~~~~~~~ ')
        produto = str(input('O nome do produto adquirido: '))
        valor = int(input('O valor do produto: '))
        total += valor
        barato += 1
        if valor >= 1000:
            mais1k += 1
        if barato == 1:   # ou 'if barato == 1 or menor > valor:' assim eliminando o segundo if!
            menor = valor
            nome = produto
        if menor > valor:
            menor = valor
            nome = produto
        q = ' '
        while not q in 'SN':
            q = str(input('Quer continuar? : ')).upper().strip()[0]
    break
print(f'O total gasto nas compra foi {total:.2f} R$\nOs produtos acima de 1000 R$ são {mais1k}\nO nome do produto mais barato é {nome} e seu preço {menor:.2f} R$')
