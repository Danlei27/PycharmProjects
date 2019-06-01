# Crie um Programa que leia vàrios nùmeros inteiros
#  pelo teclado.No final da execução, mostre a mèdia
#  entre todos os valores e qual foi o maior e o menor
#  valores lidos.O programa deve perguntar ao usuário
#  se ele quer ou não continuar a digitar valores.
cont = soma = 0
p = 'S'
while not p != 'S' and p != 'N':
    n = int(input('Digite um nùmero:'))
    p = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    soma += n
    cont += 1
    if cont == 1:
        menor = n
        maior = n
    if menor > n:
        menor = n
    if maior < n:
        maior = n
    while p != 'S' and p != 'N' :
        p = str(input('Opção  invalida! Digite novamente [S/N] para continuar: ')).strip().upper()[0]
print('FIM\nVocê digitou {} nùmeros e sua média foi {:.2f}\nO menor valor é {}\nO maior valor é {} '.format(cont,soma/cont,menor,maior))
