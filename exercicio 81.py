#Crie um programa que vai ler vários nùmeros e colocar em uma
#lista .Depois disso, mostre:
#A) Quantos nùmeros foram digitados.
#B) A lista de valores, ordenado de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.
lista = []
while  True:
        lista.append(int(input('Digite um valor: ')))
        r = str(input('Quer continuar [S/N]')).strip().upper()[0]
        if r == 'N':
          break
lista.sort(reverse=True)
print(f'Os nùmeros digitado da lista foram {len(lista)}\nOs nùmeros em ordem decrescente são {lista}\nO valor 5 ',end='')
print(f'faz parte da lista!' if lista.count(5) >= 1 else 'não está lista!')








