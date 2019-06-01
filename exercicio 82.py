#crie um programa que vai ler vários nùmeros e colocar em uma lista.
#Depois disso, cria duas listas extras que vão conter apenas os valores
# pares eos valores impares digitados,respctivamente.
#Ao final, mostre o conteúdo das três listas gerada.
lista = []
pares = []
impares = []
while True:
    lista.append(int(input('Digite um valor: ')))
    r = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
    if r in 'N':
        break
for num in lista:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
print(f'A lista completa é {lista}\nA lista de  pares são {pares}\nA lista de  ímpares foram {impares}')